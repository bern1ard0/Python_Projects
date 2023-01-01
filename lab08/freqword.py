"""
A module for representing information about words in a corpus.
"""

from gc import get_count
from typing_extensions import Self


class FreqWord:
    """
    A class representing a word and its count.
    """

    # _text is a string, _count is an int
    __slots__ = ["_text", "_count"]

    def __init__(self, text, count):
        """
        Constructor for the FreqWord class.
        """
        self._text = text
        self._count = int(count) #int function needed to store as integer

    def getText(self):
        """
        Accessor method to get text of the word

        >>> FreqWord('contemplate', 100).getText()
        'contemplate'
        >>> FreqWord('', 0).getText()
        ''
        """
        return self._text

    def getCount(self):
        """
        Accessor method to get frequency of the word

        >>> FreqWord('contemplate', 100).getCount()
        100
        >>> FreqWord('', 0).getCount()
        0
        """
        return self._count

    def __str__(self):
        """
        A method that converts an instance of the Result
        class into an easily readable string.

        >>> print(FreqWord("moo", 5))
        moo[5]
        """
        return "{}[{}]".format(self._text,self._count)


    def hasPrefix(self, prefix):
        """
        Returns whether the text starts with the given prefix or not.

        >>> FreqWord('contemplate', 100).hasPrefix('con')
        True
        >>> FreqWord('contemplate', 100).hasPrefix('tempt')
        False
        """
        return self._text[0:len(prefix)] == prefix   


    def __repr__(self):
        """
        This is a special method that helps Python print lists of WordFreq
        objects in a nice way.  Do not modify this method.
        """
        # Just invoke the __str__ method to create a nice string.
        return self.__str__()



    def matchesPattern(self, pattern):
        """
        Returns whether the text matches the given pattern or not.
    
        >>> FreqWord('contemplate', 100).matchesPattern('c***emp*at*')
        True
        >>> FreqWord('contemplate', 100).matchesPattern('contemp**')
        False
        >>> FreqWord('test', 100).matchesPattern('text')
        False
        >>> FreqWord('test', 100).matchesPattern('ne*t')
        False
        """
        if len(pattern)==len(self._text):        #checks length first
            for i in range(len(pattern)):        #iterates over range of lenght of pattern
                if pattern[i] != self._text[i] and pattern[i]!="*":
                    return False                 #checks if a single character is fails test
            return True                          #returns true after iteration is done
        return False                             



# The following two functions are defined outside of the class, so that
# we can use them as the key functions when sorting.

def textKey(freqWord):
    """
    A function that can be used as a sorting key function.
    It extracts the text from FreqWords.

    >>> words = [ FreqWord("b",5), FreqWord("c",10), FreqWord("a", 8) ]
    >>> sorted(words, key = textKey)
    [a[8], b[5], c[10]]
    """
    return freqWord.getText()

def countKey(freqWord):
    """
    A function that can be used as a sorting key function.
    It extracts the count from FreqWords.

    >>> words = [ FreqWord("b",5), FreqWord("c",10), FreqWord("a", 8) ]
    >>> sorted(words, key = countKey)
    [b[5], a[8], c[10]]
    """
    return freqWord.getCount()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
