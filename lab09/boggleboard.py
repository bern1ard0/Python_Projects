"""
Extends the Board class with specific features required for Boggle
"""

from graphics import *
from brandom import *
from boggleletter import BoggleLetter
from board import Board

class BoggleBoard(Board):
    """Boggle Board class implements the functionality of a Boggle board.
    It inherits from the Board class and extends it by creating a grid
    of BoggleLetters, shaken appropriately to randomize play."""

    __slots__ = ['_grid', "_cubes"]

    def __init__(self, win):
        super().__init__(win, rows=4, cols=4)
        #initialize grid of Boardletters
        self._grid=[]
        for col in range(self._cols):
            grid_col=[]
            for row in range(self._rows):
                #create new BoggleLtter of specific grid cord
                letter=BoggleLetter(win,col,row)

                #add Boggleletter to column
                grid_col.append(letter)

            #add column to grid
            self._grid.append(grid_col)
        
        self._cubes =  [[ "A", "A", "C", "I", "O", "T" ],
                        [ "T", "Y", "A", "B", "I", "L" ],
                        [ "J", "M", "O", "Qu", "A", "B"],
                        [ "A", "C", "D", "E", "M", "P" ],
                        [ "A", "C", "E", "L", "S", "R" ],
                        [ "A", "D", "E", "N", "V", "Z" ],
                        [ "A", "H", "M", "O", "R", "S" ],
                        [ "B", "F", "I", "O", "R", "X" ],
                        [ "D", "E", "N", "O", "S", "W" ],
                        [ "D", "K", "N", "O", "T", "U" ],
                        [ "E", "E", "F", "H", "I", "Y" ],
                        [ "E", "G", "I", "N", "T", "V" ],
                        [ "E", "G", "K", "L", "U", "Y" ],
                        [ "E", "H", "I", "N", "P", "S" ],
                        [ "E", "L", "P", "S", "T", "U" ],
                        [ "G", "I", "L", "R", "U", "W" ]]
        self.shakeCubes()


    def getBoggleLetterAtPoint(self, point):
        """
        Return the BoggleLetter that contains the given point in the window,
        or None if the click is outside all letters.

        >>> win = GraphWin("Boggle", 400, 400)
        >>> board = BoggleBoard(win)
        >>> pointIn_0_0 = Point(board.getXInset() + board.getSize() / 2, \
                                board.getYInset() + board.getSize() / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_0_0) == board._grid[0][0]
        True
        >>> pointIn_1_2 = Point(board.getXInset() + board.getSize() * 3 / 2, \
                                board.getYInset() + board.getSize() * 5 / 2)
        >>> board.getBoggleLetterAtPoint(pointIn_1_2) == board._grid[1][2]
        True
        >>> win.close()
        """
        #checks if point is present in grid
        if self.inGrid(point):
            (col, row) = self.getPosition( (point.getX(), point.getY()) )
            return self._grid[col][row]

        #returns None for click outside all letters
        else:
            return None

    def resetColors(self):
        """
        Unclicks all boggle letters on the board without changing any
        other attributes.
        """
        for x in range(self._cols):
            for y in range(self._rows):
                # gets letter out of grid and reset's it's color
                let = self._grid[x][y]
                let.setColor('black')

    def reset(self):
        """
        Clears the boggle board by clearing letters,
        clears all text areas (right, lower, upper) on board
        and resets the letters on board by calling shakeCubes.
        """
        for x in range(self._cols):
            for y in range(self._rows):
                # get letter out of grid and reset it
                let = self._grid[x][y]
                let.setLetter("")
        self.clearLowerText()
        self.clearTextArea()
        self.clearUpperText()
        self.shakeCubes()

    def shakeCubes(self):
        """
        Shakes the boggle board and sets letters
        as described by the handout.
        """
        final_list=[]
        count=0

        #iterate over shuffled cube list.
        for cubelist in shuffled(self._cubes):
            #append a random letter in each cubelist into final_list
            final_list.append(cubelist[randomInt(0,len(cubelist)-1)])

        for x in range(self._cols):
            for y in range(self._rows):
                # gets letter out of grid and sets a value
                let = self._grid[x][y]
                let.setLetter(final_list[count])
                #iterating over final_list
                count+=1

    def __str__(self):
        """
        Returns a string representation of this BoggleBoard
        """
        board = ''
        for r in range(self._rows):
            for c in range(self._cols):
                boggleLetter = self._grid[c][r]
                color = boggleLetter.getColor()
                letter = boggleLetter.getLetter()
                board += '[{}:{}] '.format(letter,color)
            board += '\n'
        return board


if __name__ == "__main__":
    from doctest import testmod
    testmod()

    # # Uncomment this code when you are ready to test it!
    #
    # # When you are ready to run on different boards,
    # # insert a call to randomize() here.  BUT you will
    # # find it much easier to test your code without
    # # randomizing things!
    #
    randomize()
    win = GraphWin("Boggle", 400, 400)
    board = BoggleBoard(win)
    print(board)

    keepGoing = True
    while keepGoing:
        pt = win.getMouse()
        if board.inExit(pt):
            keepGoing = False
        elif board.inGrid(pt):
            (col, row) = board.getPosition((pt.getX(), pt.getY()))
            print("{} at {}".format(board._grid[col][row], (col, row)))
