'''
Brennon Laney
05/20/21

'''

from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name('Brennon', 'Laney') == 'Laney;Brennon'
    assert make_full_name('Bob', 'Sid') == 'Sid;Bob'
    assert make_full_name('Joe-smo', 'Carpenter') == 'Carpenter;Joe-smo' 

def test_extract_given_name():
    assert extract_given_name('Laney;Brennon') == 'Brennon'
    assert extract_given_name('Sid;Bob') == 'Bob'
    assert extract_given_name('Carpenter;Joe-smo') == 'Joe-smo'

def test_extract_family_name():
    assert extract_family_name('Laney;Brennon') == 'Laney'
    assert extract_family_name('Sid;Bob') == 'Sid'
    assert extract_family_name('Carpenter;Joe-smo') == 'Carpenter'



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])