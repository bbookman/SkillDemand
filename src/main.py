from datetime import datetime
import ssl, pdb
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException
import copy
import logging
from constants import *
from urllib3.exceptions import NewConnectionError

matching_titles = set()
missing_titles = set()

def make_date_string():
    stamp = datetime.now()
    date_string = stamp.strftime('%Y-%d-%m-%H-%M-%S')
    return date_string

def make_time_string():
    stamp = datetime.now()
    time_string = stamp.strftime('%H:%M')
    return time_string

logging.basicConfig(filename='execution_{date}.log'.format(date = make_date_string()), level=logging.INFO)
ssl._create_default_https_context = ssl._create_unverified_context


def _start_driver():
    #d = make_date_string()          # service_args=["--verbose", "--log-path=\\log_string]
    #log_string = f'chromedriver-{d}.log'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920x1080')
    try:
        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
    except SessionNotCreatedException as e:
        print('SessionNotCreatedException - try again')
        logging.debug(e)
        try:
            driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
        except SessionNotCreatedException as s:
            print('Terminating')
            logging.debug(s)
    return driver


def _build_site_url(site_id, template, title, salary='', zipcode='', radius='30', age='60'):
    """ Makes an url with each query item inserted into the url template

    template: type = str, the url template.  example: 'http://indeed.com?{}&afg=&rfr=&title={}'
    title: type = str, job title using escape characters that are site dependent.  example: 'software+quality+engineer'
    salary: type = str, example: '100000'
    zipcode: type = str, ZIP CODE
    radius: type = str, represents the radius of the job search. example: '50'  (miles)
    age: type = str, the number of days the job description has been posted.  example: '30' (days)

    returns an url string
    """
    if site_id == 'indeed' or site_id =='ziprecruiter' or site_id == 'stackoverflow':
        return template.format(title = title, salary = salary, zipcode = zipcode, radius = radius, age = age)
    if site_id == 'careerbuilder':
        cbtitle = _build_job_title(title, '-')
        title = _build_job_title(title, '+')
        return template.format(title = title, salary = salary, zipcode = zipcode, radius = radius, age = age, cbtitle = cbtitle)

def _build_job_title(title, title_separator):
    """ Takes list of title words and adds site specific separator between words
    title: string
    separator: type = string
    returns string
    """
    result =''
    words = title.split()
    for word in words:
        result+= word + title_separator
    return result[:-1]


def get_skills(skip_dups, geo, skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip, threshold=90, radius='50', age='60'):
    """
    :param skip_dups, bool, some job titles are unique enough to skip processing duplicates. To skip set True
    :param site_id: string, site identification such as "indeed" or "monster"
    :param site_url_template: string, url template that will form the request to the job site
    :param title:  string, desired job title
    :param title_separator: string, each site may separate the job titles uniquely, for example indeed has title urls like title:='my-title-is-separated-by-dashes'
    :param title_selector: string, the xpath or other method of finding the title
    :param salaries: list, a list of strings for salary query.  example: ['50000', '100000', '200000']
    :param geo: string, nice name of geographic location.  example "San Francisco", "Austin, Texas"
    :param zip_codes: list of strings.  zip codes for the geo.  can be retrieved from https://catalog.data.gov/dataset/bay-area-zip-codes
    :param weights: dictionary of keyword and value pairs.  keywords are those desired in the title.  values are the weights (see threshold)
    :param threshold: int.  the weight threshold
    :param radius: string, search radius for each zip.  defaults to 30
    :param age: string, how old can the job postings be. defaults to 60
    UPDATES the global skills_dict

    """
    global matching_titles
    for skill in skill_keywords:
        skill_counts.setdefault(skill, 0)
    job_title = _build_job_title(title, title_separator)
    found_match_on_page = False
    not_met = 0
    for page in range(1, 4):
        #skip if too many not met
        if not_met == 7:
            print(f'{geo}: TOO MANY NOT MET, SKIPPING')
            not_met = 0
            break
        job_links = list()
        if site_id == 'indeed':
            url = _build_site_url( site_id, site_url_template, job_title, salary, zip, radius, age,)
        if site_id == 'careerbuilder':
            url = _build_site_url( site_id, site_url_template, title, salary, zip, radius, age,)
            url += f'page_number={page}'
            try:
                driver = _start_driver()
                no_more_pages = driver.find_element_by_xpath("//h3[contains(text(),'Sorry, no results were found based upon your search')]")
                driver.quit()
                if no_more_pages:
                    break
            except NoSuchElementException:
                continue

        if site_id == 'ziprecruiter':
            url = _build_site_url(site_id, site_url_template, job_title, salary, zip, radius, age, )
            url += f'page={page}'
        if site_id == 'stackoverflow':
            url = _build_site_url(site_id, site_url_template, job_title, salary, zip, radius, age, )
            url += f'pg={page}'
        try:
            print(f'geo:{geo}, site:{site_id}, page:{page}, url:{url}')
            browser = _start_driver()
            browser.get(url)

        except TimeoutException:
            print(f'TimeoutException: {url}')
            break
        except ConnectionRefusedError as c:
            #print(f'ConnectionRefusedError: {url} \n {c}')
            logging.info(f'ConnectionRefusedError: {url} \n {c}')
            print(f'ConnectionRefusedError: {url} \n {c}')
        except NewConnectionError as n:
            #print(f'NewConnectionError: {url} \n {n}')
            logging.debug(f'NewConnectionError: {url} \n {n}')

        for title_index in range(1,26):
            no_such = 0
            jtitles = list()
            try:
                if site_id == 'indeed' or site_id ==  'stackoverflow':
                    job_links = browser.find_elements_by_class_name(title_selector)
                    jtitles = [link.text for link in job_links if link.text not in missing_titles]
                    hrefs = [link.get_attribute('href') for link in job_links if title_selector in link.get_attribute('href') ]
                if site_id == 'careerbuilder':
                    job_links.append(browser.find_element_by_xpath(title_selector.format(title_index)))
                    jtitles = [link.text for link in job_links if link.text not in missing_titles]
                    hrefs = [link.get_attribute('href') for link in job_links]
                if site_id == 'ziprecruiter' or site_id == 'stackoverflow':
                    job_links = [a for a in browser.find_elements_by_tag_name('a') if title_selector in a.get_attribute('class')]
                    jtitles = [link.text for link in job_links if link.text not in missing_titles]
                    hrefs = [link.get_attribute('href') for link in job_links]
            except NoSuchElementException as e:
                element = title_selector.format(title_index)
                logging.info(f'NoSuchElementException: {element} \n {e}')
                print(f'NoSuchElementException: {element} - ITS OKAY')
                no_such+=1
                if no_such >= 4:
                    print(f'{geo}: TOO MUCH NO SUCH ELEMENT, SKIPPING')
                    logging.info('TOO MUCH NO SUCH ELEMENT, SKIPPING')
                    break
            for index, t in enumerate(jtitles):
                t = re.sub(r"(?<=[A-z])\&(?=[A-z])", " ", t)
                t = re.sub(r"(?<=[A-z])\-(?=[A-z])", " ", t)
                if skip_dups and t in missing_titles:
                    print(f'{geo}: SKIPPING duplicates')
                    break
                evaluate = t.split()
                match = 0
                for word in evaluate:
                    for keyword, value in weights.items():
                        if keyword.lower() == word.lower():
                            match += value
                if match < threshold:
                    missing_titles.add(t)
                    print(f'{geo}: THRESHOLD NOT MET: {t}')
                    not_met +=1
                    logging.debug(f'THRESHOLD NOT MET: {t}')
                else:
                    print(f'{geo}: MET THRESHOLD: {t}')
                    found_match_on_page = True
                    if skip_dups and t in matching_titles:
                        print(f'Skipping duplicate: {t}')
                        logging.debug(f'Skipping duplicate: {t}')
                        break
                    matching_titles.add(t)
                    try:
                        job_description_url = hrefs[index]
                        print(f'JD url: {url}')
                    except IndexError:
                        print('IndexError for hrefs')
                        break
                    try:
                        new_tab = _start_driver()
                        new_tab.get(job_description_url)
                        body = new_tab.find_element_by_tag_name('body').text
                        new_tab.quit()
                    except ConnectionRefusedError as c:
                        print(f'ConnectionRefusedError: {url}\n{c}')
                        logging.info(f'ConnectionRefusedError: {url}\n{c}')
                        break
                    #except TimeoutException as t:
                    #    print(f'TimeoutException: {url}')
                    #    logging.debug(t)
                    #    break

                    sbody = body.split()
                    for skill in skill_keywords:
                        for word in sbody:
                            if skill.lower() == word.lower():
                                skill_counts[skill] += 1
                                print(f'{geo}: {title}, skill: {skill}')
                                #print(f'MATCHING TITLES: {t} \n\n{matching_titles}\n\nTITLE IN MATCHING TITLES{is_in}')
                                break
            if site_id == 'indeed' or site_id == 'ziprecruiter' or site_id == 'stackoverflow':
                    break
        browser.quit()
        if site_id == 'indeed':
            break
        if not found_match_on_page:
            print(f'{geo} {zip} NO MATCHES FOUND ON PAGE {page}, SKIPPING')
            break
    return skill_counts

if __name__ == "__main__":
    start = make_time_string()
    skill_summary = dict()
    salaries = dict()
    zcode = dict()
    area = dict()
    titles = dict()

    for site_id in SITES_DICT.keys():
        stime = make_time_string()
        print(f'PROGREAM START {stime} ')
        logging.info(f'START {site_id}: {stime} ')
        title_separator = SITES_DICT[site_id]['title_word_sep']
        title_selector = SITES_DICT[site_id]['title_selector']
        site_url_template = SITES_DICT[site_id]['url_template']
        for title in TITLES.keys():
            skip_dups = TITLES[title][2]
            skill_keywords = TITLES[title][1]
            weights = TITLES[title][0]
            titles.setdefault(title, 'DEFAULT TITLE')
            for geo in GEO_ZIPS.keys():
                time = make_time_string()
                print(f'PROGREAM START WAS {site_id}: {stime} ')
                print(f'START GEO:{geo}: {time} ')
                logging.info(f'START GEO:{geo}: {time} ')
                for salary in SITES_DICT[site_id]['salaries']:
                    time = make_time_string()
                    print(f'START SALARY:{salary}: {time} ')
                    logging.info(f'START SALARY:{salary}: {time} ')
                    if site_id =='careerbuilder':
                        salaries.setdefault(salary+'000', dict())
                    else:
                        salaries.setdefault(salary, dict())
                    for zip in GEO_ZIPS[geo]:
                        print(f'zip:{zip}')
                        zip = str(zip)
                        zcode.setdefault(zip, dict())
                        skill_counts = dict()
                        skill_counts = get_skills(skip_dups, geo, skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip,)
                        for skill, value in skill_counts.items():
                            skill_summary.setdefault(skill,0)
                            skill_summary[skill] += value
                        cp = copy.deepcopy(skill_summary)
                        for k, v in cp.items():
                            if v == 0:
                                skill_summary.pop(k)
                        zcode[zip] = skill_summary
                    if site_id == 'careerbuilder' and len(salary)<=3:
                        salary+= '000'
                    salaries[salary] = zcode
                    #with open(f'{salary}-RESULTS.txt', 'w') as file:
                    #    file.write(str(salaries))
                    #    file.close()
                area[geo] = salaries
                print(f'END GEO: {geo}: {time}')
                logging.info(f'END GEO: {geo}: {time}')
                gs = geo.split()
                g = ''
                for word in gs:
                    g+=word+'_'
                with open(f'{g}RESULTS.txt', 'w') as file:
                    file.write(str(area))
                    file.close()
            titles[title] = area
            with open(f'{title}_{g}-RESULTS.txt', 'w') as file:
                file.write(str(titles))
                file.close()
            time = make_time_string()
            print(f'END TITLE {title}: {time}')
            logging.info(f'END TITLE {title}: {time}')
        time = make_time_string()
        print(f'END {site_id}: {time} ')
        logging.info(f'END {site_id}: {time} ')


    print(f'PROGRAM START TIME:{stime}')
    logging.info(f'PROGRAM START TIME:{stime}')
    end = make_time_string()
    print(f'PROGRAM END TIME:{end}')
    logging.info(f'PROGRAM END TIME:{end}')

with open(f'{title}_{geo}_RESULTS.txt', 'w') as file:
    file.write(str(titles))
    file.close()
