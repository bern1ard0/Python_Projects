"""
Module to implement auto complete
"""

import csv
from logging import critical
from freqword import *
from result import *

class AutoComplete:
    """
    A class for generating autocomplete suggestions
    """

    __slots__ = [ "_words" ]

    def __init__(self, corpus):
        """
        Constructor for the AutoComplete class. The input
        corpus corresponds to a filename to be used as a basis
        for constructing the frequency of words dictionary.

        >>> AutoComplete("data/miniGutenberg.csv")._words[0]
        circumstances[107]
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2]
        wooded[8]
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2].getText()
        'wooded'
        >>> AutoComplete("data/miniGutenberg.csv")._words[-2].getCount()
        8
        """
        with open(corpus) as csvfile:    #open file(corpus) to be read
            List=[line.strip().split(',') for line in csvfile]   
        self._words=sorted([FreqWord(word[0],word[1]) for word in List],key=textKey) #sorted(by text) list of freqWord 


    def _matchWords(self, criteria):
        """
        Part 3 of Lab:
        Perform a search to return a list of word objects that match
        the given criteria -- when the criteria corresponds to a prefix,
        this returns a list where each word contains the given prefix.

        Part 4 of Lab:
        if the criteria corresponds to a pattern (contains *'s), this
        returns a list where each word matches the given pattern.

        >>> AutoComplete("data/miniGutenberg.csv")._matchWords("sc")
        [scold[3], scraped[21]]
        >>> AutoComplete("data/miniGutenberg.csv")._matchWords("um")
        []
        """
        list=[]
        if criteria.isalpha():  #check if criteria contains only alphanumeric characters
            for word in self._words:
                if word.hasPrefix(criteria):    #finds words with similar prefix as criteria
                    list.append(word)  
            return list                #returns list of words
        else:                    #else if criteria has to do with pattern,
            for word in self._words: 
                if word.matchesPattern(criteria):     #finds words with similar pattern
                    list.append(word)
            return list             #returns list of those words

        

    def suggestCompletions(self, inputString):
        """
        Suggest word completions based on (i) whether the user has input
        a criteria or a wild card expression and (ii) frequency of occurrence
        of the possible completions. The final object that is returned is
        an instance of the Result class with the top 3 completions if at least
        3 possible completions exist (and fewer if there are less than 3 possible
        completions.) Remember that if the inputString is itself a possible completion
        it should be given top priority regardless of its frequency.

        >>> print(AutoComplete("data/gutenberg.csv").suggestCompletions("auto"))
        auto --> autonomy[7] | autocratic[5] | auto[3]
        >>> print(AutoComplete("data/miniGutenberg.csv").suggestCompletions("woo*e*"))
        woo*e* --> wooden[37] | wooded[8]
        >>> print(AutoComplete("data/gutenberg.csv").suggestCompletions("woo*e*"))
        woo*e* --> wooden[37] | woolen[15] | wooded[8]
        """
        matchedlist=self._matchWords(inputString)   #creates list of words that match with suggestion
        finallist=sorted(matchedlist, key=countKey, reverse=True)[0:3] #sorts that list in decreasing order of Frequency
        return Result(inputString, finallist)        #prints using format of the Result class

    def __str__(self):
        """
        >>> print(AutoComplete("data/miniGutenberg.csv"))
        circumstances[107]
        scold[3]
        scraped[21]
        wooded[8]
        wooden[37]
        """
        return "\n".join([str(word) for word in self._words])   #\n used to get to the next line while str used to return string


if __name__ == "__main__":
    # Run all the doctests
    import doctest
    doctest.testmod()

    # Suggest completions for any input strings provided on the command
    # line.  Eg:
    #
    #    python3 autocomplete.py moo cow r***s
    #
    import sys
    auto = AutoComplete("data/gutenberg.csv")
    for inputString in sys.argv[1:]:
        print(auto.suggestCompletions(inputString))
