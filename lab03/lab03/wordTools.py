# Replace this line with a one-line description of this module.
"""Contains various functions that are useful in solving word puzzles. """
# This publicly documents the module:
"""
Contains 6 functions:
letters:Takes as input a string phrase and returns a string
that contains just the letters from phrase (in order)
canon:Takes as input a string word and returns a "canonical" version
of word: just the letters, in lower case, and in alphabetical order
(as a string). Supports anagram testing.
uniques:Takes as input string word and return a string consisting of the unique
characters in word.
isIsogram:Takes as input a string word and returns True only if the
characters in word are unique (i.e., there are no repeated characters).
Note that case should be ignored (i.e., E and e are the same character).
sized: Takes as input a word length,n, and a word list,wordlist, and returns
a list of the words in wordlist that are exactly lenght n.
readWords: Takes as input the path to a file filename, opens and reads the words
(one per line) in that file, and returns a list containing those words.
"""

# All functions go below here.
def letters(phrase):
    """Takes as input a string phrase and returns a string
    that contains just the letters from phrase (in order).

    >>> letters('superb: owl!')
    'superbowl'
    >>> letters('')
    ''
    >>> letters('#@$%')
    ''
    """
    result = ''
    for char in phrase:
        if char.isalpha():  # if char is a letter
            result += char  # concatenate to result
    return result

def canon(word):
    """Takes as input a string word and returns a "canonical" version
    of word: just the letters, in lower case, and in alphabetical order
    (as a string). Supports anagram testing.

    >>> canon('fix me') # fix this broken doctest
    'efimx'
    >>> canon('Mamma Mia!')
    'aaaimmmm'
    >>> canon('iAm')
    'aim'
    >>> canon('a lot')
    'alot'
    """
    word = letters(word)      # drop anything that's not a letter (e.g. spaces)
    lowerWord = word.lower()  # to ensure Carol == carol
    orderedWord = sorted(lowerWord) # ie.  a *list* of letters, in alpha order
    result = ''.join(orderedWord) # converts list of letters to a single string
    return result

def uniques(word):
    """Takes as input string word and return a string consisting of the unique
    characters in word.

    >>> uniques('abracadabra')
    'abrcd'
    >>> uniques('Connecticut')
    'Conectiu'
    """
    result=''
    for x in word:
        if x not in result:
            result+=x
    return result

def isIsogram(word):
    """Takes as input a string word and returns True only if the
    characters in word are unique (i.e., there are no repeated characters).
    Note that case should be ignored (i.e., E and e are the same character).

    >>> isIsogram('Bernard')
    False
    >>> isIsogram('napiol3')
    True
    """
    result=word.lower()
    if uniques(result)==result:
        return True
    else:
        return False



def sized(n, wordList):
    """ Takes as input a word length,n, and a word list,wordlist, and returns
    a list of the words in wordlist that are exactly lenght n.
    >>> sized(3,['cat','dog','goat'])
    ['cat', 'dog']
    >>> sized(5,['moose','messi','ronaldo'])
    ['moose', 'messi']
    """
    result=[]
    for x in wordList:
        if n==len(x):
            result.append(x)
    return result





def readWords(filename):
    """Takes as input the path to a file filename, opens and reads the words
    (one per line) in that file, and returns a list containing those words.

    >>> len(readWords('words/firstNames.txt'))
    5166
    >>> readWords('words/bodyparts.txt')[14]
    'belly button'
    >>> sized(8, readWords('words/italianCities.txt'))
    ['Cagliari', 'Florence', 'Siracusa']
    """
    results = []
    with open(filename) as wordFile:
        for line in wordFile:
            word = line.strip()   # do not use letters (think: 'belly button')
            results.append(word)  # add on to results list
    return results

if __name__ == '__main__':
    # the following code tests the tests in the docstrings ('doctests').
    # as you add tests, re-run this as a script to test your work
    from doctest import testmod  # this import is necessary when testing
    testmod(verbose=True)                    # test this module, according to the doctests
