"""Implements the logic of the game of boggle."""

from graphics import GraphWin
from boggleboard import BoggleBoard
from boggleletter import BoggleLetter
from brandom import randomize

class BoggleGame:

    __slots__ = [ "_validWords", "_board", "_foundWords", "_selectedLetters" ]

    def __init__(self, win):
        """
        Create a new Boggle Game and load in our lexicon.
        """
        # set up the set of valid words we can match
        self._validWords = self.__readLexicon()

        # init other attributes here.
        self._board = BoggleBoard(win)
        self._board.shakeCubes()
        self._foundWords = []
        self._selectedLetters = []

    def __readLexicon(self, lexiconName='bogwords.txt'):
        """
        A helper method to read the lexicon and return it as a set.
        """
        validWords = set()
        with open(lexiconName) as f:
          for line in f:
            validWords.add(line.strip().upper())

        return validWords

    #private method to convert selectedLetters to string
    def __letterconvert(self):
        string = ''
        for boggleletter in self._selectedLetters:
            string += boggleletter.getLetter()
        return string

    #private method to simplify adding letter to word
    def __addletter(self, letter):
        self._selectedLetters.append(letter)
        self._board.addStringToLowerText(letter.getLetter())
        letter.setColor("blue") #set recent letter blue

    #private method to simplify restarting a new word without reseting game
    def __startnewword(self):
        self._selectedLetters = []
        self._board.resetColors()
        self._board.clearLowerText()

    def doOneClick(self, point):
        """
        Implements the logic for processing one click.
        Returns True if play should continue, and False if the game is over.
        """
        # These steps are one way to think about the design, although
        # you are free to do things differently if you prefer.

        # step 1: check for exit button and return False if clicked
        if self._board.inExit(point):
            return False
        # step 2: check for reset button and reset
        elif self._board.inReset(point):
            self._board.reset()
            self._board.resetColors()
            self._foundWords = []
            self._selectedLetters = []

        # step 3: check if click is on a cell in the grid
        elif self._board.inGrid(point):
            # get BoggleLetter at point
            letter = self._board.getBoggleLetterAtPoint(point)

            # if this is the first letter in a word being constructed,
            # add letter and display it on lower text of board
            if self._selectedLetters == []:
                self.__addletter(letter) #calls private method above

            # elif adding a letter to a non-empty word, make sure it's adjacent
            # and not already in word. Then, update state
            elif self._selectedLetters != []:
                #must be adjacent and a unique letter
                if (letter.isAdjacent(self._selectedLetters[-1])
                and letter.getLetter() not in self.__letterconvert()):
                    #set previous letter to green
                    self._selectedLetters[-1].setColor("green")
                    self.__addletter(letter) #calls private method above

                # elif clicked on same letter, end word and check for validity
                elif letter == self._selectedLetters[-1]:
                    word = self.__letterconvert() #calls private method above
                    if ((len(word) >= 3) #at least 3 letters
                    and (word not in self._foundWords) #no repeat words
                    and (word in self.__readLexicon('bogwords.txt'))): #validity
                        self._board.addStringToTextArea(word)
                        self._board.addStringToTextArea("\n")
                        self._foundWords.append(word)
                        self.__startnewword() #calls private method above
                #else; not adjacent or pre-existing letter is clicked; restart.
                else:
                    self.__startnewword() #calls private method above
        # return True to indicate we want to keep playing
        return True

if __name__ == '__main__':

    # When you are ready to run on different boards,
    # insert a call to randomize() here.  BUT you will
    # find it much easier to test your code without
    # randomizing things!
    randomize()
    win = GraphWin("Boggle", 400, 400)
    game = BoggleGame(win)
    keepGoing = True
    while keepGoing:
        point = win.getMouse()
        keepGoing = game.doOneClick(point)
