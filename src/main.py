from datetime import datetime
import ssl
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

_driver = start_driver()

def get_jd_links(url, xpath_template):
    """
    :param url: string , website url
    :param xpath:  string, xpath
    :return: list of selenium webdriver objects
    """
    links = []
    _driver.get(url)
    for i in range(1,500):
        try:
            links.append(_driver.find_element_by_xpath(xpath_template.format(i)))
        except NoSuchElementException:
            element = xpath_template.format(i)
            logging.info(f'NoSuchElementException: {element}')
            continue
    return links


def get_tiles(links):
    """
    :param links: list of selenium web objects contining the job title url
    :return: list of multi-word titles
    """
    return [link.text for link in links]


def build_site_url(template, title, salary='', zipcode='', radius='30', age='30'):
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


def build_title_only_url(template, title):
    return template.format(title)

def filter_titles(title_dict, links, threshold):
    """ Uses title key words and a weight for each word to evaluate matching job titles

    title_dict: type = dict, keys are single word parts of a job title and values represent
                weight for each word
    links: type = list, a list of job description links to evaluate
    threshold: type = int, add the weights and if they meet or exceed this threshold then
               the job title is considered a match

    returns a list of matching links
    """
    result = []
    for link in links:
        total = 0
        for key, value in title_dict.items():
            title = link.text
            in_title = key in title
            logging.debug(f'title: {title}, key: {key}, in_title?: {in_title}')
            if key.lower() in title.lower():
                total += value
        if total >= threshold:
            logging.debug('Threshold met, appending:{title}')
            result.append(link)
    return result

def get_bodies(site_id, urls):
    bodies = []
    for url in urls:
        if site_id =='monster':
            try:
                href = url.get_attribute('href')
                _driver.get(href)
            except StaleElementReferenceException:
                url_str = str(url)
                logging.info(f'StaleElementReferenceException: {url_str}')
                print('StaleElementReferenceException')
                continue

            body = _driver.find_element_by_tag_name('body').text
        if site_id == 'indeed':
            url.click()
            body = _driver.find_element_by_tag_name('body').text
        bodies.append(body)
    return bodies



def build_job_title(title_words, separator):
    """ Takes list of title words and adds site specific separator between words
    title_words: type = list
    separator: type = string
    returns string
    """
    result =''
    for word in title_words:
        result+= word + separator
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



#TODO: Remove below prior to production

def test__flow(site_id):
    logging.info(f'TEST: {site_id}')
    template = SITES_DICT[site_id]['url_template']
    sep = SITES_DICT[site_id]['title_word_sep']
    title = build_job_title(['software', 'quality', 'assurance', 'engineer'], sep)
    url = build_site_url(template, title , '120000', '95032', '60', '60')
    xpath_template = SITES_DICT[site_id ]['xpath_template']
    logging.info('Getting links')
    links = get_jd_links(url, xpath_template)
    title_dict = {'software': 30, 'quality': 80, 'assurance': 90, 'qa': 100, 'sqa': 100, 'sdet': 100, 'test': 70,
                  'automation': 70, 'engineer': 20}
    logging.info('Filtering links')
    filtered_links = filter_titles(title_dict, links, 90)
    if filtered_links:
        logging.info('Got filtered links')
    bodies = get_bodies('monster', filtered_links)
    if bodies:
        logging.info('Got bodies. Total: ' +  str(len(bodies)))

test__flow('indeed')
