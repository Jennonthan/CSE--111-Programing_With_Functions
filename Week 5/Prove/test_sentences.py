'''
Brennon Laney
05/19/21
prove
purpose: test sentences.py using pytest 
'''




from hashlib import new
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, \
    get_punctuation
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # Test the singular nouns.
    singular_nouns = ['adult', 'bird', 'boy', 'car', 'cat',
        'child', 'dog', 'girl', 'man', 'woman']
    # This loop will repeat the statements inside it 4 times.
    for _ in range(10):
        word = get_noun(1)

        assert word in singular_nouns


    # Test the plural nouns.
    plural_nouns = ['adults', 'birds', 'boys', 'cars', 'cats',
        'children', 'dogs', 'girls', 'men', 'women']
    for _ in range(10):
        word = get_noun(2)

        assert word in plural_nouns

def test_get_verb():
    # Test the singular verbs in the present.
    singular_present_verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
        'runs', 'sleeps', 'talks', 'walks', 'writes']
    # This loop will repeat the statements inside it 4 times.
    for _ in range(10):
        word = get_verb(1, 'present')

        assert word in singular_present_verbs


    plural_present_verbs = ['drink', 'eat', 'grow', 'laugh', 'think',
        'run', 'sleep', 'talk', 'walk', 'write']
    for _ in range(10):
        word = get_verb(2, 'present')

        assert word in plural_present_verbs


    past_verbs = ['drank', 'ate', 'grew', 'laughed', 'thought',
        'ran', 'slept', 'talked', 'walked', 'wrote']
    for _ in range(10):
        word = get_verb(1, 'past')

        assert word in past_verbs

    # Test the plural determiners.
    future_verbs = ['will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write']
    for _ in range(10):
        word = get_verb(1, 'future')

        assert word in future_verbs

def test_get_preposition():
    '''
    This will randomly select a preposition using the get_preposition
    function to see if it is in the list of prepositions below
    '''
    prepositions = ['about', 'above', 'across', 'after','along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    for _ in range(10):
        word = get_preposition()

        assert word in prepositions



def test_get_prepositional_phrase():
    # This is the list of prepositions
    prepositions = ['about', 'above', 'across', 'after','along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']

    # This is the list of singular nouns
    singular_nouns = ['adult', 'bird', 'boy', 'car', 'cat',
        'child', 'dog', 'girl', 'man', 'woman']

    # This is the list of plural nouns
    plural_nouns = ['adults', 'birds', 'boys', 'cars', 'cats',
        'children', 'dogs', 'girls', 'men', 'women']

    # This is the list of singular determiners
    singular_determiners = ["the", "one"]

    # This is the list of plural determiners
    plural_determiners = ["some", "many"]


    # This sees if the singular prepositional phrase contains the correct
    #words. It does this by spliting the sentence and compairing the words 
    #the lists of words
    for _ in range(600):
        phrase = get_prepositional_phrase(1)

        new_phrase = phrase.split(' ')
        preposition = new_phrase[0]
        determiner = new_phrase[1]
        noun = new_phrase[2]

        # This sees if the preposition is in the preposition list
        assert preposition in prepositions

        # This sees if the determiner is in its list
        assert determiner in singular_determiners

        # This sees if the noun is in its list
        assert noun in singular_nouns


    # This sees if the plural prepositional phrase contains the correct
    #words. It does this by spliting the sentence and compairing the words 
    #the lists of words above
    for _ in range(600):
        phrase = get_prepositional_phrase(2)

        new_phrase = phrase.split(' ')
        preposition = new_phrase[0]
        determiner = new_phrase[1]
        noun = new_phrase[2]

        # This sees if the preposition is in the preposition list
        assert preposition in prepositions
        
        # This sees if the determiner is in its list
        assert determiner in plural_determiners
        
        # This sees if the noun is in its list
        assert noun in plural_nouns


def test_get_punctuation():
    punctuation = ['.', '!', '?', '!!']

    # This will test to see if the punctuation is in the
    #list of punctuation 
    for _ in range(4):
        punctuation01 = get_punctuation()
        assert punctuation01 in punctuation


pytest.main(['-v', 'test_sentences.py'])