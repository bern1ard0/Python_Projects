"""
Lab 7, Task 1

Accumulating recursion with lists of strings.
Inspired by https://stackoverflow.com/questions/3021/what-is-recursion-and-when-should-i-use-it
"""

def firstSentence(object, subject):
    """Given the strings object and subject, return a string representing the
    first sentence of the story about those characters."""
    return  "The mother of the " + object + " told " + \
            "a story about a " + subject + "..."

def lastSentence(object):
    """Given the string object, return a string representing the second (last)
    sentence of the story about that character."""
    return "and then the " + object + " fell asleep."

def bedtimeStory(characters):
    """
    Main (recursive) function for producing a bedtime story based on a list of
    strings (story characters). Returns a list of strings where each element is
    a sentence in the bedtime story.

    >>> bedtimeStory(['ant', 'fly'])
    ['The mother of the ant told a story about a fly...', 'and then the ant fell asleep.']
    >>> bedtimeStory(['Bernard', 'Wongibe'])
    ['The mother of the Bernard told a story about a Wongibe...', 'and then the Bernard fell asleep.']
    """
    # Replace this line with your code:
    if len(characters)<=1:            #base condition
        return []
    else:
        #recursive step
        return [firstSentence(characters[0],characters[1])] + bedtimeStory(characters[1:]) + [lastSentence(characters[0])]
def formatPrint(storyList):
    """Given a list of strings as story list, prints out the full story to the
    terminal in a nicely indented fashion."""
    n = len(storyList)

    # Print the first half of the list, with increasing indentation.
    for i in range(n // 2):
        print("   " * i + storyList[i])

    # Print the second half of the list, with decreasing indentation.
    for i in range(n // 2, n):
        print(("   " * (n - i - 1)) + storyList[i])

# Run the doctests, and also generate a list of characters from you provide
# when you run your program from the terminal.  Eg:
# 
#    python3 bedtime.py parrot flamingo heron cow
#
if __name__ == "__main__":
    """Testing code"""
    from doctest import testmod
    testmod()

    from sys import argv
    chars = argv[1:]
    formatPrint(bedtimeStory(chars))
