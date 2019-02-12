from .main import *
from selenium import webdriver

'''
Designed for pytest.  Probably can use unittest as well or nosetest
'''

def test_parse_site_for_jd_links():
    url = 'https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose,+CA&fromage=300&limit=50&sort=&psf=advsrch'
    xpath_template = '//*[@id="sja{}"]'
    p = parse_site_for_jd_links(url, xpath_template)
    assert isinstance(p, list)


def test_build_site_url():
    template = 'TITLE:{title}, SALARY:{salary}, LOCATION:{zipcode}, DISTANCE:{radius}, POST_AGE:{age}'
    title = 'test_title'
    salary = 'test_salary'
    zipcode = 'test_location'
    radius = 'test_distance'
    age = 'test_age'
    result = build_site_url(template, title, salary, zipcode, radius, age)
    expected ='TITLE:test_title, SALARY:test_salary, LOCATION:test_location, DISTANCE:test_distance, POST_AGE:test_age'
    assert result == expected

def test_filter_titles():
    title_dict = {'software': 30, 'quality': 80, 'assurance': 90, 'qa': 100, 'sqa': 100, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
    links = [
        'software',
        'software quality',
        'software quality assurance',
        'http://www.blah.com?fred="sdet"'
        'automation quality'
    ]
    expected = [
        'software quality',
        'software quality assurance',
        'http://www.blah.com?fred="sdet"'
        'automation quality'
    ]
    threshold = 90
    result = filter_titles(title_dict, links, threshold)
    assert result == expected


def test_get_related_titles():
    links = [
        'http://blah.com&title=Fred+Flintstone</a>',
        'http://wee.com?h=foo&t=bar&title=Barny Rubbel</a>'
    ]
    title_start= 'title='
    title_end = '</a>'
    expected = ['Fred+Flintstone', 'Barny Rubbel']
    result = get_related_titles(title_start, title_end, links)
    assert result == expected

def test_build_job_title():
    title_words = [
    'Hello',
    'world',
    '!'
    ]
    seperator = '+'
    expected = 'Hello+world+!'
    result = build_job_title(title_words, seperator)
    assert result == expected

def test_remove_stop_words():
    list_of_texts = [
    'this is a body of <b>text</b> and has some stop words as well as non-stop words',
    'SDET  Java Python the and of a'
    ]
    expected = [



    ]

    result = remove_stop_words(list_of_texts)

def test_remove_html_from_bodies():
    bodies = [
        'this body contains <a href> HTML <b> that should <b>be removed</b>  <div> <script></script> ',
        '<h1 style="color: blue"> Hello world! </h1>',
        '<style>h1 { color: blue;</style>My favorite'
    ]
    expected = [

    ]

    result = remove_html_from_bodies(bodies)
    assert result == expected

def test_get_skill_counts_unique_appearance_of_skill():
    bodies = [
        'this body should produce a count of one for java java java and not three or more java java javascript'
    ]
    skill_list = [
        'java'
    ]
    expected = {
    'java':1
    }
    result = get_skill_counts(bodies, skill_list)
    assert result == expected

def test_get_skill_counts():
    bodies = [

    ]

    skill_list = [

    ]

    expected = [

    ]
    result = get_skill_counts(bodies, skill_list)
    assert result == expected

def test_build_title_only_url():
    template = 'http://hithere.com?{}&oh'
    title = 'TITLE'
    expected = 'http://hithere.com?TITLE&oh'
    result = build_title_only_url(template, title)
    assert result == expected

def test_remove_superflous(string_list, superflous_strings):
    string_list = [


    ]
    expected = [

    ]
    result = remove_superflous(string_list, superflous_strings)
    assert result == expected
