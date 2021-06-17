'''
Brennon Laney
05/18/21
purpose: Import the prefix and sufix functions from the 
word library and test them to see if they work
'''

from words import prefix, suffix
import pytest

def test_prefix():
    '''verify that the prefix function works'''
    assert prefix('', 'correct') == ''
    assert prefix('', '') == ''
    assert prefix('clear', '') == ''
    assert prefix('happy', 'funny') == ''
    assert prefix('cat', 'catalog') == 'cat'
    assert prefix('dogmatic', 'dog') == 'dog'
    assert prefix('jump', 'joyous') == 'j'
    assert prefix('unwise', 'ungrateful') == 'un'
    assert prefix('disable', 'distasteful') == 'dis'


def test_suffix():
    '''verify that the suffix function works'''
    assert suffix('', '') == ''
    assert suffix('', 'correct') == ''
    assert suffix('clear', '') == ''
    assert suffix('angelic', 'awesome') == ''
    assert suffix('found', 'profound') == 'found'
    assert suffix('ditch', 'itch') == 'itch'
    assert suffix('happy', 'funny') == 'y'
    assert suffix('tired', 'fatigued') == 'ed'
    assert suffix('swimming', 'FLYING') == 'ing'


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.

pytest.main(['-v', '--tb=line', '-rN', 'test_words.py'])