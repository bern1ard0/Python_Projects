# Script includes functions with logic errors
"""
This program tests whether or not a word is "vowelacious".  We call
a word vowelacious if it contains 3 or more consecutive vowels.
"""


# Change these three strings to be examples where isVowelaciousBuggy1
# properly identifies a vowelacious word, properly identifies a 
# non-vowelacious word, and misclassifies a vowelacious word as
# not vowelacious:
buggy1Vowelacious = "leai"    # string is vowelacious; function returns True 
buggy1NotVowelacious = "lepi" # string is not vowelacious; function returns False
buggy1Bad = "leain"            # string is vowelacious; function returns False


# Change these three strings to be examples where isVowelaciousBuggy2
# properly identifies a vowelacious word, properly identifies a 
# non-vowelacious word, and misclassifies a vowelacious word as
# not vowelacious:
buggy2Vowelacious = "" #there is none   # string is vowelacious; function returns True 
buggy2NotVowelacious = "bena" # string is not vowelacious; function returns False
buggy2Bad = "beai"            # string is vowelacious; function returns False


def isVowelaciousBuggy1(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This version has a logic error.
    TODO: DESCRIBE THE LOGIC ERROR!
    The problem here is that the variable containing the consecutive vowels gets reset
    in case there is a consonant after that series of vowels. 
    """
    #print('isVowelaciousBuggy1({})'.format(word)) # debugging print
    vowelSeq = '' # initializing variable to accumulate vowel seq

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
        else:
            vowelSeq = '' # reset if a consonant occurs
        #print('vowelSeq =', vowelSeq) # debugging print

    return len(vowelSeq) >= 3

def isVowelaciousBuggy2(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This version has a logic error.
    TODO: DESCRIBE THE LOGIC ERROR!
    The problem here is that the else statement after the elif statement
    will reset vowelSeq to an empty string value as long as the len of vowelSeq is not 3.
    Meaning, it wouldn't be take up to an iteration of 2 and will already be reset to an
    empty string value. 
    """

    #print('isVowelaciousBuggy2({})'.format(word)) # debugging print
    vowelSeq = '' # initializing variable to accumulate vowel seq
    found = False # initialize return value

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
        elif len(vowelSeq) >= 3:
            #print("Setting found to true") # debugging print
            found = True
        else:
            vowelSeq = '' # reset if a consonant occurs
        #print('vowelSeq =', vowelSeq) # debugging print

    return found

def isVowelacious(word):
    """Takes a word as input and is supposed to return True if
    the word is vowelacious (contain 3 or more consecutive vowels).
    This is the correct version.
    """
    vowelSeq = '' # initializing variable to accumulate vowel seq
    found = False # initialize return value

    for char in word:
        if char.lower() in 'aeiou':
            vowelSeq += char # add char
        elif len(vowelSeq) >= 3:
            #print("Setting found to true") # debugging print
            found = True
        elif char.lower() not in 'aeiou':
            vowelSeq = '' # reset if a consonant occurs
        #print('vowelSeq =', vowelSeq) # debugging print

    return found
    

if __name__ == "__main__":
    # call the functions on some test cases directly
    print(isVowelaciousBuggy1("hello"))
    print(isVowelaciousBuggy2("world"))
    print(isVowelacious("vowelaciousiuosly"))
