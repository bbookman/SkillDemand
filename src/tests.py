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

#TODO Remove hardcoded keywords if UI happens

def test_keywords():
    assert KEYWORDS
    assert isinstance(KEYWORDS, list)
    is_string = [True for keyword in KEYWORDS if isinstance(keyword, str)]
    assert is_string

