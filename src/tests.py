from .main import *
from .constants import *



def test_site_root_urls_exist():
    assert INDEED_ROOT_URL
    assert isinstance(INDEED_ROOT_URL, str)


def test_site_query_terms_exists():
    expected = [
        INDEED_TITLE_QUERY_TERM,
        INDEED_JOB_TYPE_QUERY_TERM,
        INDEED_SALARY_QUERY_TERM,
        INDEED_LOCATION_QUERY_TERM,
        INDEED_DISTANCE_QUERY_TERM,
        INDEED_JOB_DESCRIPTION_AGE_QUERY_TERM,
    ]
    is_string = [True for item in expected if isinstance(item, str)]
    assert expected
    assert all(is_string)

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
    result = test_build_site_url(template, title, jobtype, salary, location,distance,age)
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
