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
    str_links =  [str(link) for link in links]
    return str_links






'''
url = 'https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose,+CA&fromage=300&limit=50&sort=&psf=advsrch'
page = urllib2.urlopen(url)
soup = beautiful(page, 'html.parser')
links = soup('a', "jobtitle turnstileLink") #INDEED_JD_LINK_FINDERS = []
parse_me = [str(link) for link in links]


for item in parse_me:
    start_title_loc = item.find('title=')
    end_title_loc = item.find('">')
    title = item[  start_title_loc + 7: end_title_loc]
    href_loc = item.find('href')
    close = item.find('>')
    href = item[href_loc + 6:close]
    hrefs.append(href)


title="Senior QA Engineer II">

<b>Senior</b> QA <b>Engineer</b> II</a>



'''