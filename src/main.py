from datetime import datetime
import ssl
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
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
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options)
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


def get_skills(skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip, threshold=90, radius='60', age='60'): #todo
    """

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
    for skill in skill_keywords:
        skill_counts.setdefault(skill, 0)

    job_title = _build_job_title(title, title_separator)
    for page in range(1, 4):
        browser = _start_driver()
        not_met = 0
        print(f'Page:{page}')
        job_links = list()
        if site_id == 'indeed':
            url = _build_site_url( site_id, site_url_template, job_title, salary, zip, radius, age,)
        if site_id == 'careerbuilder':
            url = _build_site_url( site_id, site_url_template, title, salary, zip, radius, age,)
            url += f'page_number={page}'
        if site_id == 'ziprecruiter':
            url = _build_site_url(site_id, site_url_template, job_title, salary, zip, radius, age, )
            url += f'page={page}'
        if site_id == 'stackoverflow':
            url = _build_site_url(site_id, site_url_template, job_title, salary, zip, radius, age, )
            url += f'pg={page}'
        try:
            browser.get(url)

        except ConnectionRefusedError as c:
            #print(f'ConnectionRefusedError: {url} \n {c}')
            logging.info(f'ConnectionRefusedError: {url} \n {c}')
            print(f'ConnectionRefusedError: {url} \n {c}')
        except NewConnectionError as n:
            #print(f'NewConnectionError: {url} \n {n}')
            logging.debug(f'NewConnectionError: {url} \n {n}')
        except WebDriverException:
            browser.quit()
            break
        try:
            no_more_pages = browser.find_element_by_xpath("//h3[contains(text(),'Sorry, no results were found based upon your search')]")
            if no_more_pages:
                print(f'NO MORE PAGES')
                break
        except NoSuchElementException:
            continue
        except WebDriverException as w:
            logging.info(f'WebDriverException \nerror: {w} \nurl: {url}')
            browser.quit()
            break
        for title_index in range(1,26):
            no_such = 0
            try:
                if site_id == 'indeed' or site_id ==  'stackoverflow':
                    job_links = browser.find_elements_by_class_name(title_selector)
                    jtitles = [link.text for link in job_links]
                    hrefs = [link.get_attribute('href') for link in job_links]
                if site_id == 'careerbuilder':
                    job_links.append(browser.find_element_by_xpath(title_selector.format(title_index)))
                    jtitles = [link.text for link in job_links]
                    hrefs = [link.get_attribute('href') for link in job_links]
                if site_id == 'ziprecruiter' or site_id == 'stackoverflow':
                    job_links = [a for a in browser.find_elements_by_tag_name('a') if title_selector in a.get_attribute('class')]
                    jtitles = [link.text for link in job_links]
                    hrefs = [link.get_attribute('href') for link in job_links]
            except NoSuchElementException as e:
                element = title_selector.format(title_index)
                logging.info(f'NoSuchElementException: {element} \n {e}')
                print(f'NoSuchElementException: {element} - ITS OKAY')
                no_such+=1
                if no_such >= 10:
                    print('TOO MUCH NO SUCH ELEMENT, SKIPPING')
                    logging.info('TOO MUCH NO SUCH ELEMENT, SKIPPING')
                    break
                continue

            for index, t in enumerate(jtitles):
                #skip if already seen  NOT APPLICABLE FOR CERTAIN JOB TITLES
                #if t in matching_titles or t in missing_titles:
                #    continue
                #skip if too many not met
                if not_met == 10:
                    print('TOO MANY NOT MET, SKIPPING')
                    logging.info('TOO MANY NOT MET, SKIPPING')
                    not_met = 0
                    break
                t = re.sub(r"(?<=[A-z])\&(?=[A-z])", " ", t)
                t = re.sub(r"(?<=[A-z])\-(?=[A-z])", " ", t)
                evaluate = t.split()
                match = 0
                for word in evaluate:
                    for keyword, value in weights.items():
                        if keyword.lower() == word.lower():
                            match += value
                if match < threshold:
                    if t in missing_titles:  #okay to skip here
                        break
                    missing_titles.add(t)
                    print(f'THRESHOLD NOT MET: {t}')
                    not_met +=1
                    logging.debug(f'THRESHOLD NOT MET: {t}')
                else:
                    #if t in matching_titles:  #NOT APPLICABLE FOR CERTAIN TITLES
                    #    continue
                    print(f'MET THRESHOLD: {t}')
                    #matching_titles.add(t)
                    logging.debug(f'MET THRESHOLD: {t}')
                    job_description_url = hrefs[index]
                    new_tab = _start_driver()
                    try:
                        new_tab.get(job_description_url)
                        body = new_tab.find_element_by_tag_name('body').text
                        new_tab.quit()
                    except ConnectionRefusedError as c:
                        print(f'ConnectionRefusedError: {url}\n{c}')
                        logging.info(f'ConnectionRefusedError: {url}\n{c}')
                        break
                    sbody = body.split()
                    for skill in skill_keywords:
                        for word in sbody:
                            if skill.lower() == word.lower():
                                skill_counts[skill] += 1
                                break
            if site_id == 'indeed' or site_id == 'ziprecruiter' or site_id == 'stackoverflow':
                    break
        if site_id == 'indeed':
            break
        browser.quit()
    return skill_counts



if __name__ == "__main__":
    start = make_time_string()
    skill_summary = dict()
    salaries = dict()
    zcode = dict()
    area = dict()
    titles = dict()

    for site_id in SITES_DICT.keys():
        time = make_time_string()
        print(f'START {site_id}: {time} ')
        logging.info(f'START {site_id}: {time} ')
        title_separator = SITES_DICT[site_id]['title_word_sep']
        title_selector = SITES_DICT[site_id]['title_selector']
        site_url_template = SITES_DICT[site_id]['url_template']
        for title in TITLES.keys():
            time = make_time_string()
            print(f'START TITLE {title}: {time}')
            logging.info(f'START TITLE {title}: {time}')
            skill_keywords = TITLES[title][1]
            weights = TITLES[title][0]
            titles.setdefault(title, 'DEFAULT TITLE')
            for geo in GEO_ZIPS.keys():
                time = make_time_string()
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
                        time = make_time_string()
                        print(f'START ZIP: {zip}: {time}')
                        logging.info(f'START ZIP: {zip}: {time}')
                        zip = str(zip)
                        zcode.setdefault(zip, dict())
                        skill_counts = dict()
                        skill_counts = get_skills(skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip,)
                        for skill, value in skill_counts.items():
                            skill_summary.setdefault(skill,0)
                            skill_summary[skill] += value
                        cp = copy.deepcopy(skill_summary)  #NOT EXACTLY WORKING AS EXPECTED
                        for k, v in cp.items():
                            if v == 0:
                                skill_summary.pop(k)
                        zcode[zip] = skill_summary
                        time = make_time_string()
                        print(f'END ZIP: {zip}: {time}')
                        logging.info(f'END ZIP: {zip}: {time}')
                    if site_id == 'careerbuilder' and len(salary)<=3:
                        salary+= '000'
                    salaries[salary] = zcode
                    time = make_time_string()
                    print(f'END SALARY {salary}: {time}')
                    logging.info(f'END SALARY {salary}: {time}')
                area[geo] = salaries
                print(f'END GEO: {geo}: {time}')
                logging.info(f'END GEO: {geo}: {time}')
            titles[title] = area
            time = make_time_string()
            print(f'END TITLE {title}: {time}')
            logging.info(f'END TITLE {title}: {time}')
        time = make_time_string()
        print(f'END {site_id}: {time} ')
        logging.info(f'END {site_id}: {time} ')


    print(f'PROGRAM START TIME:{start}')
    logging.info(f'PROGRAM START TIME:{start}')
    end = make_time_string()
    print(f'PROGRAM END TIME:{end}')
    logging.info(f'PROGRAM END TIME:{end}')

with open('RESULTS.txt', 'w') as file:
    file.write(str(titles))
