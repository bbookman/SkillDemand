from main import *
from constants import *

'''
Designed for pytest.  Probably can use unittest as well or nosetest
'''

def test_site_root_urls_exist():
    assert INDEED_ROOT_URL
    assert isinstance(INDEED_ROOT_URL, str)

def test_site_template_url():
    assert INDEED_URL_TEMPATE
    assert isinstance(INDEED_URL_TEMPATE, str)
    expected = 'https://www.indeed.com/jobs?as_and=TITLE&jt=FULLTIME&salary=100000&radius=100&l=LOCATION&fromage=AGE&limit=LIMIT&psf=advsrch'
    test_url = INDEED_URL_TEMPATE.format('TITLE', 'FULLTIME', '100000', '100', 'LOCATION', 'AGE', 'LIMIT')
    assert expected == test_url

#TODO Remove hardcoded keywords if UI happens, hence test below is invalid

def test_keywords():
    assert KEYWORDS
    assert isinstance(KEYWORDS, list)
    is_string = [True for keyword in KEYWORDS if isinstance(keyword, str)]
    assert is_string

def test_parse_site_for_jd_links():
    url = 'https://www.indeed.com/jobs?as_and=senior+technical+support+engineer&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=fulltime&st=&as_src=&salary=145000&radius=100&l=San+Jose,+CA&fromage=300&limit=50&sort=&psf=advsrch'
    link_finders = ['a', "jobtitle turnstileLink"]
    p = parse_site_for_jd_links(url, link_finders)
    assert isinstance(p, list)
    assert isinstance(p[0], str)

def test_build_site_url():
    template = 'TITLE:{}, JOBTYPE:{}, SALARY:{}, LOCATION:{}, DISTANCE:{}, POST_AGE:{}'
    title = 'test_title'
    jobtype = 'test_jobtype'
    salary = 'test_salary'
    location = 'test_location'
    distance = 'test_distance'
    age = 'test_age'
    result = test_build_site_url(template, title, salary, location, distance, age, jobtype )
    expected ='TITLE:test_title, JOBTYPE:test_jobtype, SALARY:test_salary, LOCATION:test_location, DISTANCE:test_distance, POST_AGE:test_age'
    assert result == expected

def test_filter_titles():
    title_dict = {'software': 30, 'quality': 80, 'assurance': 90, 'qa': 100, 'sqa': 100, 'sdet': 100, 'test': 70, 'automation': 70, 'engineer': 20}
    links = [
        'software',
        'software quality',
        'software qualit assurance',
        'http://www.blah.com?fred="sdet"'
        'automation quality'
    ]
    expected = [
        'software qualit assurance',
        'http://www.blah.com?fred="sdet"'
        'automation quality'
    ]
    threshold = 90
    result = filter_titles(title_dict, links, threshold)
    assert result == expected

def test_get_jd_bodies():
    result = get_jd_bodies(urls)
    assert isinstance(result, list)
    assert isinstance(result[0], str)

def test_get_related_titles():
    links = [
        'http://blah.com&title=Fred+Flintstone',
        'http://wee.com?h=foo&t=bar&title=Barny Rubbel'
    ]
    expected = ['Fred+Flintstone', 'Barny Rubbel']
    result = get_related_titles(title_locator, links)
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
