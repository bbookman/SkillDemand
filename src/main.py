import urllib.request as urllib2
from bs4 import BeautifulSoup as beautiful
from constants import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

INDEED_URL_TEMPATE = 'https://www.indeed.com/jobs?as_and={}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt={}&st=&as_src=&salary={}&radius={}&l={}fromage={}&limit=500&sort=&psf=advsrch'

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


def build_site_url(template, title, jobtype, salary, location, distance, age):
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
    return template.format(title, jobtype, salary, location, distance, age)

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
