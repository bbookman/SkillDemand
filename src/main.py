import urllib.request as urllib2
from bs4 import BeautifulSoup as beautiful
from constants import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def parse_site_for_jd_links(url, link_finders):
    page = urllib2.urlopen(url)
    soup = beautiful(page, 'html.parser')
    links = soup(link_finders[0], link_finders[1])
    str_links = [str(link) for link in links]
    return str_links


def build_site_url(template, title, jobtype, salary, location, distance, age):
    return template.format(title, jobtype, salary, location, distance, age)

def filter_titles(title_dict, links, threshold):
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
    bodies = []
    for url in urls:
        page = urllib2.urlopen(url)
        soup = beautiful(page, 'html.parser')
        body = soup('body')
        bodies.append(str(body))
    return bodies
