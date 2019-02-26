from datetime import datetime
import ssl
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import copy
import logging
from constants import *

def make_date_string():
    stamp = datetime.now()
    date_string = stamp.strftime('%Y-%d-%m-%H-%M-%S')
    return date_string

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
    if site_id == 'indeed':
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


def get_bodies(site_id, site_url_template, title, title_separator, title_selector, salary, skilllist, title_dict, threshold, radius='30', age='60'):
    """

    :param site_id: string, site identification such as "indeed" or "monster"
    :param site_url_template: string, url template that will form the request to the job site
    :param title:  string, desired job title
    :param title_separator: string, each site may separate the job titles uniquely, for example indeed has title urls like title:='my-title-is-separated-by-dashes'
    :param title_selector: string, the xpath or other method of finding the title
    :param salaries: list, a list of strings for salary query.  example: ['50000', '100000', '200000']
    :param geo: string, nice name of geographic location.  example "San Francisco", "Austin, Texas"
    :param zip_codes: list of strings.  zip codes for the geo.  can be retrieved from https://catalog.data.gov/dataset/bay-area-zip-codes
    :param title_dict: dictionary of keyword and value pairs.  keywords are those desired in the title.  values are the weights (see threshold)
    :param threshold: int.  the weight threshold
    :param radius: string, search radius for each zip.  defaults to 30
    :param age: string, how old can the job postings be. defaults to 60
    UPDATES the global skills_dict

    """
    skill_dict = dict()
    for skill in skilllist:
        skill_dict.setdefault(skill, 0)
    browser = _start_driver()
    job_title = _build_job_title(title, title_separator)
    for page in range(1, 5):
        if site_id == 'indeed':
            url = _build_site_url( site_id, site_url_template, job_title, salary, zip, radius, age,)
        if site_id == 'careerbuilder':
            url = _build_site_url( site_id, site_url_template, title, salary, zip, radius, age,)
            url += f'page_number={page}'
        browser.get(url)
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

        for title_index in range(26):
            try:
                if site_id == 'indeed':
                    job_links = browser.find_elements_by_class_name(title_selector)
                if site_id == 'careerbuilder':
                    job_links = list()
                    job_links.append(browser.find_element_by_xpath(title_selector.format(title_index)))
            except NoSuchElementException:
                element = title_selector.format(title_index)
                logging.info(f'NoSuchElementException: {element}')
                print(f'NoSuchElementException: {element}')
                continue

            jtitles = [link.text for link in job_links]
            hrefs = [link.get_attribute('href') for link in job_links]
            for index, t in enumerate(jtitles):
                print(f'Checking: {title}')
                logging.info(f'Checking: {t}')
                t = re.sub(r"(?<=[A-z])\&(?=[A-z])", " ", t)
                t = re.sub(r"(?<=[A-z])\-(?=[A-z])", " ", t)
                evaluate = t.split()
                match = 0
                for word in evaluate:
                    for keyword, value in title_dict.items():
                        if keyword.lower() == word.lower():
                            match += value
                            logging.debug(f'Matched keyword: {keyword}, value: {value}, match: {match}')
                if match < threshold:
                    print(f'THRESHOLD NOT MET: {t}')
                    logging.info(f'THRESHOLD NOT MET: {t}')
                    continue
                else:
                    print(f'MET THRESHOLD: {t}')
                    logging.info(f'MET THRESHOLD: {t}')
                    job_description_url = hrefs[index]
                    new_tab = _start_driver()
                    new_tab.get(job_description_url )
                    body = new_tab.find_element_by_tag_name('body').text
                    new_tab.close()
                    sbody = body.split()
                    for skill in skilllist:
                        for word in sbody:
                            logging.debug(f'Check skill:{skill} == word:{word}')
                            if skill.lower() == word.lower():
                                logging.info(f'Found skill:{skill}')
                                print(f'Found skill:{skill}')
                                skill_dict[skill] += 1
                                break

            if site_id == 'indeed':
                    break
        if site_id == 'indeed':
            break
        browser.close()
        browser.quit()
    return skill_dict




results = dict()
location = dict()
income = dict()
geo = 'San Francisco Bay Area'
results.setdefault(geo, 'San Francisco Bay Area')

jobtitle = 'software quality assurance engineer'
skilllist = SKILL_KEYWORDS_QA
title_dict = {'software': 50, 'quality': 60, 'assurance': 30, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
threshold = 90

site_id = 'indeed'
title_separator = SITES_DICT[site_id]['title_word_sep']
title_selector = SITES_DICT[site_id]['title_selector']
salaries = ['50000', '100000', '150000']

site_url_template = SITES_DICT[site_id]['url_template']
zips = SF_ZIPS


for salary in salaries:
    print(f'THIS SALARY {salary} ')
    zcode = dict()
    print(f'THIS SALARY {salary} ')
    for zip in zips:
        print(f'THIS ZIP {zip}')
        skill_counts = get_bodies(site_id, site_url_template, jobtitle, title_separator, title_selector, salary,
                                  skilllist, title_dict, threshold, radius='30', age='60')
        # remove zeros
        cp = copy.deepcopy(skill_counts)
        for k, v in cp.items():
            if v == 0:
                skill_counts.pop(k)
        zcode[zip] = skill_counts
income[salary] = zcode
location[geo] = income
results[jobtitle] = location

with open('indeedRESULTS.txt', 'w') as file:
    file.write(str(results))

'''
site_id = 'careerbuilder'
title_separator = SITES_DICT[site_id]['title_word_sep']
title_selector = SITES_DICT[site_id]['title_selector']
salaries = ['50', '100', '150']
site_url_template = SITES_DICT[site_id]['url_template']
zips = SF_ZIPS

print(f'THIS GEO {geo} ')
for salary in salaries:
    print(f'THIS SALARY {salary} ')
    zcode = dict()
    for zip in zips:
        print(f'THIS ZIP {zip}')
        skill_counts = get_bodies(site_id, site_url_template, jobtitle, title_separator, title_selector, salary,
                                  skilllist, title_dict, threshold, radius='30', age='60')
        #remove zeros
        cp = copy.deepcopy(skill_counts)
        for k, v in cp.items():
            if v == 0:
                skill_counts.pop(k)
        zcode[zip] = skill_counts
    salary = salary + '000'
    income[salary] = zcode
location[geo] = income
logging.info(f'location:{location}')
results[jobtitle] = location




with open('cbRESULTS.txt', 'w') as file:
    file.write(str(results))

'''






print('DONE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')