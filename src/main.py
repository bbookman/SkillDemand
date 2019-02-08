import urllib.request as urllib2
from bs4 import BeautifulSoup as beautiful
from constants import *


def parse_site_for_jd_links(url, link_finders):
    """
    :param url:
    :return: links:
    """
    page = urllib2.urlopen(url)
    soup = beautiful(page, 'html.parser')
    links = soup(link_finders[0], link_finders[1])
    str_links = [str(link) for link in links]
    return str_links


def build_site_url(template, title, jobtype, salary, location, distance, age):
    return template.format(title, jobtype, salary, location, distance, age)
