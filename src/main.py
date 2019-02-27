from datetime import datetime
import ssl
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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


def get_skills(skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip, threshold=90, radius='30', age='60'):
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
    browser = _start_driver()
    job_title = _build_job_title(title, title_separator)
    for page in range(1, 5):
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
            logging.debug(f'ConnectionRefusedError: {url} \n {c}')
        except NewConnectionError as n:
            #print(f'NewConnectionError: {url} \n {n}')
            logging.debug(f'NewConnectionError: {url} \n {n}')
        '''
        print("----------------------------------------------")
        print(f'title:{job_title.upper()}')
        print(f'Page:{page}')
        print(f'salary: {salary}')
        print(f'zip:{zip}')
        print(f'URL: {url}')
        print("----------------------------------------------")
  
        logging.info("----------------------------------------------")
        logging.info(f'title:{job_title}')
        logging.info(f'Page:{page}')
        logging.info(f'salary: {salary}')
        logging.info(f'zip:{zip}')
        logging.info(f'URL: {url}')
        logging.info("----------------------------------------------")

        '''
        for title_index in range(1,26):
            job_links = list()
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
            except NoSuchElementException:
                element = title_selector.format(title_index)
                logging.debug(f'NoSuchElementException: {element}')
                print(f'NoSuchElementException: {element}')
                continue

            #jtitles = [link.text for link in job_links]
            #hrefs = [link.get_attribute('href') for link in job_links]
            for index, t in enumerate(jtitles):
                #skip if already seen
                if t in matching_titles or t in missing_titles:
                    #print(f'ALREADY SEEN: {t}')
                    continue
                t = re.sub(r"(?<=[A-z])\&(?=[A-z])", " ", t)
                t = re.sub(r"(?<=[A-z])\-(?=[A-z])", " ", t)
                evaluate = t.split()
                match = 0
                for word in evaluate:
                    for keyword, value in weights.items():
                        if keyword.lower() == word.lower():
                            match += value
                if match < threshold:
                    #print(f'THRESHOLD NOT MET: {t}')
                    missing_titles.add(t)
                    #logging.info(f'THRESHOLD NOT MET: {t}')
                    continue
                else:

                    if t in matching_titles:
                        continue
                    print(f'MET THRESHOLD: {t}')
                    matching_titles.add(t)
                    #logging.info(f'MET THRESHOLD: {t}')
                    job_description_url = hrefs[index]
                    new_tab = _start_driver()
                    try:
                        new_tab.get(job_description_url)
                        body = new_tab.find_element_by_tag_name('body').text
                        new_tab.close()
                    except ConnectionRefusedError:
                        print(f'ConnectionRefusedError: {url}')
                        logging.info(f'ConnectionRefusedError: {url}')
                        break
                    sbody = body.split()
                    for skill in skill_keywords:
                        for word in sbody:
                            if skill.lower() == word.lower():
                                skill_counts[skill] += 1
                                #logging.info(f'site_id: {site_id}, zip:{zip}, title: {title}, skill:{skill}, count: {skill_counts[skill]}')
                                #print(f'site_id: {site_id}, zip:{zip}, title: {title}, skill:{skill}, count: {skill_counts[skill]}')
                                break

            if site_id == 'indeed':
                    break
        if site_id == 'indeed':
            break
       # browser.close()
       # browser.quit()
    return skill_counts



if __name__ == "__main__":
    start = make_time_string()
    skill_summary = dict()
    salaries = dict()
    zcode = dict()
    area = dict()
    titles = dict()

    for site_id in SITES_DICT.keys():
        title_separator = SITES_DICT[site_id]['title_word_sep']
        title_selector = SITES_DICT[site_id]['title_selector']
        site_url_template = SITES_DICT[site_id]['url_template']
        for title in TITLES.keys():
            skill_keywords = TITLES[title][1]
            weights = TITLES[title][0]
            titles.setdefault(title, 'DEFAULT TITLE')
            for skill in skill_keywords:
                skill_summary.setdefault(skill,0)
            for geo in GEO_ZIPS.keys():
                for salary in SITES_DICT[site_id]['salaries']:
                    if site_id == 'careerbuilder':
                        salary+= '000'
                    salaries.setdefault(salary,0)
                    for zip in GEO_ZIPS[geo]:
                        zip = str(zip)
                        zcode.setdefault(zip, dict())
                        skill_counts = dict()
                        skill_counts = get_skills(skill_counts, site_id, site_url_template, title, title_separator, title_selector, salary, skill_keywords, weights, zip,)
                        for skill, value in skill_counts.items():
                            skill_summary[skill] += value
                    cp = copy.deepcopy(skill_summary)
                    for k, v in cp.items():
                        if v == 0:
                            skill_counts.pop(k)
                    zcode[zip] = skill_summary
                salaries[salary] = zcode
            area[geo] = salaries
        titles[title] = area
    print(f'START TIME:{start}')
    logging.info(f'START TIME:{start}')
    end = make_time_string()
    print(f'END TIME:{end}')
    logging.info(f'END TIME:{end}')
    print(titles)




'''

with open('cbRESULTS.txt', 'w') as file:
    file.write(str(results))

'''





