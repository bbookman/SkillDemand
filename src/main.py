from datetime import datetime
import ssl
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import StaleElementReferenceException
#from nltk.tokenize import sent_tokenize, word_tokenize
import logging
from constants import *

def make_date_string():
    stamp = datetime.now()
    date_string = stamp.strftime('%Y-%d-%m-%H-%M-%S')
    return date_string

logging.basicConfig(filename='execution_{date}.log'.format(date = make_date_string()), level=logging.INFO)
ssl._create_default_https_context = ssl._create_unverified_context


def start_driver():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=chrome_options)
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


def remove_stop_words(list_of_texts):
    """ Removes English stop words from the body of job description
    use:

        https://pythonspot.com/tokenizing-words-and-sentences-with-nltk/
        https://pythonspot.com/nltk-stop-words/

    bodies: type = list of strings

    returns: list of SINGLE WORD strings with stop words removed
    """
    pass

def remove_html_from_bodies(bodies):
    """ Removes html tags from body of job description

    possibly use:
        https://tutorialedge.net/python/removing-html-from-string/
        https://rushter.com/blog/python-fast-html-parser/
        https://community.esri.com/thread/207202-how-to-use-beautiful-soup-to-remove-html-tags-from-arcgis-metadata
        https://www.dotnetperls.com/remove-html-tags-python
        https://www.laurivan.com/strip-html-tags-in-python/
        https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
        https://bytes.com/topic/python/answers/33816-easy-way-remove-html-entities-html-document

    bodies: type = list of strings
    return: list of SINGLE WORD strings with as much html and javascript removed as possible
    """
    pass

def get_skill_counts(bodies, skill_list):
    """ Counts the UNIQUE time a skill is present in the body of a job description

    bodies: list of strings
    skill_list: list of strings to match / count
    returns: dictionary.  Keys are the skill, values are the total counts for
             each instance a skill appears once in a job body

    example result:
        {'java': 30, 'maven: 3', 'python': 28}  .. this means there were 30 job descriptions
        which used the word java ONCE

    hint:  LOWERCASE the bodies, the skill list, and the results using string.lower()
    """
    pass

def remove_superflous(string_list, superflous_strings):
    """ Removes unnecessary strings such as "director" and "manager"
    Because "director of software engineering" is more or less the same as "manager of software engineering"

    string_list: type = list, strings to filter
    superflous_strings: type = list, strings to remove

    returns list of strings
    """
    pass


def get_bodies(site_id, site_url_template, title, title_separator, title_selector, salaries, geo, zip_codes, title_dict, threshold, radius='30', age='60'):
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
    :return: results dictionary with data model:

        [Geo]
           [Zip]
            [Salary]: list of bodies of job description pages that match desired job title..
                      should be further processed by  get_skill_counts()
                      ultimately replace the bodies with a DICTIONARY
                      where keys are the job skill (ex: 'Java') and the value is the total count of that
                      skill for the salary range

        Example:

        ['San Francisco': ['95054' : ['50000': (bodyA, bodyB, bodyC)] ] ]

        Should become

         ['San Francisco': ['95054' : ['50000': ['Java': 40, 'python': 24, 'pandas': 15] ] ]

    """
    body_count = 0
    results = dict()
    income = dict()
    zcode = dict()
    for salary in salaries:
        income.setdefault(salary, list())
    for code in zip_codes:
        zcode.setdefault(code, dict())

    browser = start_driver()
    new_tab = start_driver()
    job_title = _build_job_title(title, title_separator)
    logging.info(f'title:{job_title}')
    print(f'title:{job_title.upper()}')
    for page in range(1,7):
        if site_id == 'careerbuilder':
            print("----------------------------------------------")
            print(f'Page:{page}')
            print("----------------------------------------------")
        for zip in zip_codes:
            print(f'zip:{zip}')
            logging.info(f'zip:{zip}')
            for salary in salaries:
                bodies = []
                print(f'salary: {salary}')
                logging.info(f'salary: {salary}')
                if site_id == 'indeed':
                    url = _build_site_url( site_id, site_url_template, job_title, salary, zip, radius, age,)
                if site_id == 'careerbuilder':
                    url = _build_site_url( site_id, site_url_template, title, salary, zip, radius, age,)
                    url += f'page={page}'
                browser.get(url)
                logging.info(f'get: {url}')

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
                            new_tab.get(job_description_url )
                            body = new_tab.find_element_by_tag_name('body').text
                            #pdb.set_trace()
                            #todo remove
                            body = body[:10]
                            #bodies.append(body)
                            body_count+=1
                            if site_id == 'indeed':
                                income[salary].append(body)
                                zcode[zip] = income
                                results[geo] = zcode
                                break
                            if site_id == 'careerbuilder':
                                income[salary].append(body)
                                continue

                    if site_id == 'indeed':
                        break

                zcode[zip] = income
                results[geo] = zcode


    logging.info('=====================================================')
    logging.info(results)
    print('=============')
    print(f'Body Count: {body_count}')
    logging.info(f'Body Count: {body_count}')
    return results




site_id = 'careerbuilder'
title_separator = SITES_DICT[site_id]['title_word_sep']
title_selector = SITES_DICT[site_id]['title_selector']
salaries = ['50', '75', '100', '150', '200']
title_dict = {'software': 50, 'quality': 60, 'assurance': 30, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
threshold = 90
site_url_template = SITES_DICT[site_id]['url_template']
geo = 'San Francisco Bay Area'
get_bodies(site_id, site_url_template, 'software quality assurance engineer', title_separator, title_selector, salaries,geo, SF_ZIPS, title_dict, threshold, radius='60',)

'''

site_id = 'indeed'
title_separator = SITES_DICT[site_id]['title_word_sep']
title_selector = SITES_DICT[site_id]['title_selector']
salaries = ['50000', '75000', '100000', '150000', '200000']
title_dict = {'software': 30, 'quality': 80, 'assurance': 10, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
threshold = 90
site_url_template = SITES_DICT[site_id]['url_template']
geo = 'San Francisco Bay Area'
get_bodies(site_id, site_url_template, 'software quality assurance engineer', title_separator, title_selector, salaries,geo, SF_ZIPS, title_dict, threshold, radius='30', age='60')
'''
