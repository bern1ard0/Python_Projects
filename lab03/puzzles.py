"""Start by solving spelling-bee puzzle B1.

   Next, you may solve either the NPR puzzle P1 or P2.  You must solve at
   least one of these! If you want extra practice, try solving both.

   Extra Credit: If you would like a challenge, check out problems B2 and P3.
   These are not required! A small amount of extra credit will be given if you
   solve one or both of them.
"""

from wordTools import canon, letters, uniques, isIsogram, readWords

def b1(filename):
    """How many lowercase 7-letter isograms are in words/dict.txt?

    This function returns an int representing the number of 7-letter isograms
    that are the answer.
    """
    count=0
    with open(filename) as wordFile:
        for word in wordFile:
            if isIsogram(word)==True and len(letters(word))==7:
                count+=1
    return count

def p1(filename):
    """Name part of the human body in six letters. Add an 'r' and rearrange
    the result to name another part of the body in seven letters.

    This function returns a string representing the concatenation of the
    two body parts (eg, 'part1 part2' or 'part2 part1').
    """
    words=readWords(filename)
    for word in words:
        if len(canon(word))==6:
            with_r= word + "r"
            cwith_r=canon(with_r)
            for wd in words:
                cnw=canon(wd)
                if cwith_r==cnw:
                    result= word +" "+ wd

    return result



def p2(filename,filename2):
    """Think of a major city in France whose name is an anagram of a major city
    in Italy.

    This function returns a string representing the concatenation of
    the cities (eg, 'frenchCity italianCity' or 'italianCity frenchCity').
    """
    french_city=readWords(filename)
    italian_city=readWords(filename2)
    for city in french_city:
        cty=canon(city)
        for citty in italian_city:
            ct=canon(citty)
            if cty==ct:
                result= city + " "+ citty
    return result

def b2():
    """Extra credit: Suppose you have a seven letter hive, 'mixcent'. How many
    4-letter lowercase words in words/dict.txt (1) include 'm' and (2) are
    spelled only using (possibly repeated) letters from the hive string?

    This function returns an int representing the number of words.
    """
    pass

def p3():
    """Extra credit: Think of a disease in five letters. Shift each letter three
    spaces later in the alphabet---for example, 'a' would become 'd', 'b' would
    become 'e', etc. The result will be a prominent name from the Bible.

    This function returns a string that is a concatenation of the illness and
    the name (eg, 'illness name' or 'name illness').
    """
    pass

if __name__ == '__main__':
    # call puzzle functions
    print("b1('words/dict.txt'): " + str(b1('words/dict.txt')))
    print("p1('words/bodyparts.txt'): " + str(p1('words/bodyparts.txt')))
    print("p2('words/frenchcities.txt','words/italiancities.txt'): " + str(p2('words/frenchcities.txt','words/italiancities.txt')))
    print("b2(): " + str(b2()))
    print("p3(): " + str(p3()))
