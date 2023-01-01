"""
Lab 7, Task 4

Implements a module which draws a tree pattern using the Python turtle.
"""

from turtle import *
from sys import argv

def initializeTurtle():
    """Setups up the window and initializes the turtle to be at the base of the
    main trunk facing north"""

    # Create a turtle window
    setup(600, 600)
    reset()

    # Configure our turtles line width and speed
    pensize(1) 
    speed(0)   # 0=fastest, 1=slowest, 6=normal

    # By default turtle starts at (0,0), the center of the screen and faces east.
    # We move it to a reasonable spot for a shrub and point it north.
    up()
    goto(-100, -200)
    left(90)
    down()


def drawShrub(trunkLength, angle, shrinkFactor, minLength):
    """
    Draws a shrub as specified in Lab 9 Task 4.
    Returns a pair (a 2-tuple) consisting of
      (1) the total number of branches (including the trunk) and
      (2) the total length of the branches (including the trunk) of the shrub.
    Assume that the turtle is positioned at the base of the main
    trunk facing north before this function is called.
    """
    # Write me!
    branchcount=0
    lenbranch=0
    if trunkLength < minLength:
        return (0,0) #no additional branch
    
    else:
        #Trunk
        branchcount+=1
        lenbranch+=trunkLength
        fd(trunkLength)
        
        # Drawing right sub trees.                                                                                                                                               
        rt(angle)
        rtBranchLen = trunkLength*shrinkFactor
        #rightbranches num and length
        numrtbranch, lenrtbranch= drawShrub(rtBranchLen, angle, shrinkFactor, minLength)
        # Drawing left subtrees.   
        ltBranchlen = shrinkFactor*rtBranchLen
        lt(angle * 2)
        #leftbranches num and length
        numltbranch, lenltbranch= drawShrub(ltBranchlen, angle, shrinkFactor, minLength) 
        # Returning to starting position                                                                                                                                 
        up(); rt(angle); bk(trunkLength); down()    
        #returning total number of branches and total length of branches                                         
        return (numrtbranch+numltbranch+1,lenrtbranch+lenltbranch+trunkLength)        
          

# When run as a script, take a picture size and the gap between
# concentric squares as command-line arguments.
if __name__=='__main__':
    """Testing code"""
    if len(argv) != 5:
        print("Provide a trunk length, angle, shrink factor, and min length, eg:\n")
        print("  python3 shrub.py 100 15 0.5 60\n")
    else:
        trunkLength = float(argv[1])
        angle = float(argv[2])
        shrinkFactor = float(argv[3])
        minLength = float(argv[4])

        initializeTurtle()
        numBranches, totalLength = drawShrub(trunkLength, angle, shrinkFactor, minLength)
        print('shrub({}, {}, {}, {}) -> ({}, {})'.format(trunkLength, angle, shrinkFactor,
                                minLength, numBranches, totalLength))
        getscreen().getcanvas().postscript(file="shrub-{}-{}-{}-{}.ps".format
                                (trunkLength, angle, shrinkFactor, minLength))

        # Comment out the line below if you want
        # the turtle screen to close automatically.
        exitonclick()
