import urllib.request as urllib2
from bs4 import BeautifulSoup as beautiful
from constants import *
import ssl
from nltk.tokenize import sent_tokenize, word_tokenize
ssl._create_default_https_context = ssl._create_unverified_context


def parse_site_for_jd_links(url, link_finders):
    """Get links for each job description

    url: type = str, a string with each url query item embeded, example 'http://indeed.com?salary=10000&jobtype=fulltime'
    link_finders: type = list, first item will almost always be 'a' for an anchor tag, second item would be a unique quality
                  identifying the urls that are for job descriptions
                  example: ['a', 'some_unique_string_identifying_job_description_urls']

    returns a list of urls as strings
    """
    page = urllib2.urlopen(url)
    soup = beautiful(page, 'html.parser')
    links = soup(link_finders[0], link_finders[1])
    str_links = [str(link) for link in links]
    return str_links


def build_site_url(template, title, salary, location, distance, age, jobtype = None):
    """ Makes an url with each query item inserted into the url template

    template: type = str, the url template.  example: 'http://indeed.com?{}&afg=&rfr=&title={}'
    title: type = str, job title using escape characters that are site dependent.  example: 'software+quality+engineer'
    jobtype: type = str, example: fulltime, partime, contract
    salary: type = str, example: '100000'
    location: type = str, using escape charactersthat are site dependent.  example: 'San+Jose,+CA'
    distance: type = str, represents the radius of the job search. example: '50'  (miles)
    age: type = str, the number of days the job description has been posted.  example: '30' (days)

    returns an url string
    """
    return template.format(title, salary, location, distance, age, jobtype)


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
        if total > threshold:
            result.append(link)
    return result

def get_jd_bodies(urls):
    """ Gets the contents of the job description page body

    urls: type = list, a list of urls for which to obtain the body text

    returns a list of body text contents for each url
    """
    bodies = []
    for url in urls:
        page = urllib2.urlopen(url)
        soup = beautiful(page, 'html.parser')
        body = soup('body')
        bodies.append(str(body))
    return bodies

def get_related_titles(title_locator, links):
    """ Allows front end to display job titles related to the one queried

    title_locator: type= string, unique query item in url indicating job title
    links: type = list, list of job description links

    returns list containing strings of job titles
    """
    titles = []
    for link in links:
        title_query_item_start_loc = link.find(title_locator)
        title_and_more = link[title_query_item_start_loc  + len(title_locator):]
        print(f'title_and_more:{title_and_more } ')
        title_end_loc = title_and_more.find('&')
        print(f'title_end_loc:{title_end_loc}')
        if title_end_loc > 0:
            title = title_and_more[:title_end_loc]
        else:
            title = title_and_more
        titles.append(title)
    return titles

def remove_stop_words_from_bodies(bodies):
    """ Removes English stop words from the body of job description
    use:

        https://pythonspot.com/tokenizing-words-and-sentences-with-nltk/
        https://pythonspot.com/nltk-stop-words/

    bodies: type = list of strings

    returns: list of strings with stop words removed
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
    return: list of strings with as much html and javascript removed as possible
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
