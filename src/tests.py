from .main import *
from .constants import *

'''
Designed for pytest.  Probably can use unittest as well or nosetest
'''


def test_build_site_url():
    template = 'TITLE:{title}, SALARY:{salary}, LOCATION:{zipcode}, DISTANCE:{radius}, POST_AGE:{age}'
    title = 'test_title'
    salary = 'test_salary'
    zipcode = 'test_location'
    radius = 'test_distance'
    age = 'test_age'
    result = _build_site_url(template, title, salary, zipcode, radius, age)
    expected ='TITLE:test_title, SALARY:test_salary, LOCATION:test_location, DISTANCE:test_distance, POST_AGE:test_age'
    assert result == expected

def test_build_job_title():
    title_words = [
    'Hello',
    'world',
    '!'
    ]
    separator = '+'
    expected = 'Hello+world+!'
    result = _build_job_title(title_words, separator)
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

def test_remove_superflous(string_list, superflous_strings):
    string_list = [


    ]
    expected = [

    ]
    result = remove_superflous(string_list, superflous_strings)
    assert result == expected
