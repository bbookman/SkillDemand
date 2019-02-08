from .constants import *


def test_site_root_urls_exist():
    assert INDEED_ROOT_URL
    assert isinstance(INDEED_ROOT_URL, str)


def test_site_title_query_terms_exists():
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
