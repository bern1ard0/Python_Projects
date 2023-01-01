"""
Module to implement a result object that will be returned by auto complete
"""

from typing import final
from freqword import *

class Result:
    """
    A class for outputting readable autocomplete suggestions
    """

    __slots__ = ["_input", "_completions"]

    def __init__(self, inputWord, completionList):
        """
        Constructor for the Result class
        """
        self._input=inputWord
        self._completions=completionList

    def __str__(self):
        """
        A method that converts an instance of the Result
        class into an easily readable string.

        >>> print(Result("the", [FreqWord("the",4), FreqWord("theirs",3), FreqWord("then",2)]))
        the --> the[4] | theirs[3] | then[2]
        """
        initial_string= "{} --> {}".format(self._input,self._completions[0])
        if len(self._completions)==1:
            return "{} --> {}".format(self._input,self._completions[0]) #incase length of list is 1, it is executed directly
        else:
            for freqword in self._completions[1:]:
                initial_string += " | "+ str(freqword)   #incase length of list is >1, it is executed iteratively
            return initial_string
            
        


if __name__ == "__main__":
    import doctest
    doctest.testmod()
