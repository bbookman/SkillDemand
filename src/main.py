from datetime import datetime
import ssl
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.common.exceptions import InvalidSessionIdException
from selenium.common.exceptions import TimeoutException, InvalidArgumentException
#from nltk.tokenize import sent_tokenize, word_tokenize
ssl._create_default_https_context = ssl._create_unverified_context
import logging

def make_date_string():
    stamp = datetime.now()
    date_string = stamp.strftime('%Y-%d-%m-%H-%M-%S')
    return date_string

logging.basicConfig(filename='execution_{date}.log'.format(date = make_date_string()), level=logging.INFO)

#GLOBALS

_job_title_list = []
_weight_dictionary = dict()
_skills = []
_title_string = ''
_salary = ''
_location =''
_radius='30'
_age = '30'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)


def parse_site_for_jd_links(url, xpath_template):
    """
    :param url: string , website url
    :param xpath:  string, xpath
    :return: list of selenium webdriver objects
    """
    links = []
    driver.get(url)
    for i in range(1,500):
        try:
            links.append(driver.find_element_by_xpath(xpath_template.format(i)))
        except NoSuchElementException:
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
            if key in link:
                total += value
        if total >= threshold:
            result.append(link)
    return result



def build_job_title(title_words, seperator):
    """ Takes list of title words and adds site specific seperator between words
    title_words: type = list
    seperator: type = string
    returns string
    """
    result =''
    for word in title_words:
        result+= word + seperator
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
