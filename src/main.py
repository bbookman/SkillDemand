from datetime import datetime
import ssl
import pdb, re
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

#GLOBALS

_job_title_list = []
_weight_dictionary = dict()
_skills = []
_title_string = ''
_salary = ''
_zipcode =''
_radius='30'
_age = '30'


def start_driver():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


def _build_site_url(template, title, salary='', zipcode='', radius='30', age='60'):
    """ Makes an url with each query item inserted into the url template

    template: type = str, the url template.  example: 'http://indeed.com?{}&afg=&rfr=&title={}'
    title: type = str, job title using escape characters that are site dependent.  example: 'software+quality+engineer'
    salary: type = str, example: '100000'
    zipcode: type = str, ZIP CODE
    radius: type = str, represents the radius of the job search. example: '50'  (miles)
    age: type = str, the number of days the job description has been posted.  example: '30' (days)

    returns an url string
    """

    return template.format(title = title, salary = salary, zipcode = zipcode, radius = radius, age = age)



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
    body_count = 0
    results = dict()
    income = dict()
    zcode = dict()
    for salary in salaries:
        income.setdefault(salary, None )
    for code in zip_codes:
        zcode.setdefault(code, None)

    browser = start_driver()
    new_tab = start_driver()
    job_title = _build_job_title(title, title_separator)
    logging.info(f'title:{job_title}')
    print(f'title:{job_title.upper()}')
    for zip in zip_codes:
        print(f'zip:{zip}')
        logging.info(f'zip:{zip}')
        for salary in salaries:
            bodies = []
            print(f'salary: {salary}')
            logging.info(f'salary: {salary}')
            url = _build_site_url(site_url_template, job_title, salary, zip, '30', '60')
            browser.get(url)
            logging.info(f'get: {url}')
            try:
                if site_id == 'indeed':
                    job_links = browser.find_elements_by_class_name(title_selector)
            except NoSuchElementException:
                element = title_selector.format(i)
                logging.info(f'NoSuchElementException: {element}')
                print(f'NoSuchElementException: {element}')
                continue
            if job_links:
                jtitles = [link.text for link in job_links]
                hrefs = [link.get_attribute('href') for link in job_links]
                for index, title in enumerate(jtitles):
                    print(f'Checking: {title}')
                    logging.info(f'Checking: {title}')
                    title = re.sub(r"(?<=[A-z])\&(?=[A-z])", " ", title)
                    title = re.sub(r"(?<=[A-z])\-(?=[A-z])", " ", title)  #(?<=[A-z])[\&\-\\]+(?=[A-z])
                    evaluate = title.split()
                    match = 0
                    for word in evaluate:
                        for keyword, value in title_dict.items():
                            if keyword.lower() == word.lower():
                                match += value
                                logging.debug(f'Matched keyword: {keyword}, value: {value}, match: {match}')
                    if match < threshold:
                        print(f'THRESHOLD NOT MET: {title}')
                        logging.info(f'THRESHOLD NOT MET: {title}')
                        continue
                    else:
                        print(f'MET THRESHOLD: {title}')
                        logging.info(f'MET THRESHOLD: {title}')
                        job_description_url = hrefs[index]
                        new_tab.get(job_description_url )
                        body = new_tab.find_element_by_tag_name('body').text
                        bodies.append(body)
                        body_count+=1
                income[salary] = bodies
                zcode[zip] = income
                results[geo] = zcode

    logging.debug(results)
    print('=============')
    print(f'Body Count: {body_count}')
    logging.info(f'Body Count: {body_count}')
    return results




#TODO: Remove below prior to production


zip_codes = [95032,

             95054, 94010,
94536,

94539,
94402,
94404,
94403,
94538,
94560,
94065,
94063,
94027,
94002,
94070,
95134,
95002,
94062,
94089,
94301,
94025,
94303,
95035,
95140,
94061,
94043,
94304,
94305,
94035,
94306,
94028,
94040,
94022,
94085,
94086,
94024,
94087]

site_id = 'indeed'
title_separator = SITES_DICT[site_id]['title_word_sep']
title_selector = SITES_DICT[site_id]['title_selector']
salaries = ['50000', '75000', '100000', '150000', '200000']
title_dict = {'software': 30, 'quality': 80, 'assurance': 10, 'qa': 80, 'sqa': 90, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
threshold = 90
site_url_template = SITES_DICT[site_id]['url_template']
geo = 'San Francisco Bay Area'
get_bodies(site_id, site_url_template, 'software quality assurance engineer', title_separator, title_selector, salaries,geo, zip_codes, title_dict, threshold, radius='30', age='60')
