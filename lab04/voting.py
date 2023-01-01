# Write documentation for this file

'''
Write documentation for this module here.
'''


# Part 1.1
def readBallot(filename):

    '''This function reads a cvs file and returns a list of lists where each
    interior list is a single ballot containing candidate names ordered from
    most prefered to least prefered.

    #doctest below
    """
    >>> readBallot('data/simple.csv')
    [['Aamir', 'Chris', 'Beth'], ['Beth', 'Aamir', 'Chris'], ['Chris', 'Beth', 'Aamir'], ['Aamir', 'Beth', 'Chris']]

    >>> readBallot('data/characters.csv')[5][3]
    'Scarlett OHara'

    >>> readBallot('data/example.csv')[3][1]
    'Cid'

    """
    '''
    with open(filename) as csvfile:
        votes=[line.strip().split(',') for line in csvfile]
    return votes


# Part 1.2
def firstChoiceVotes(ballots):
    ''' Takes in a list of lists of individual ballots. Each of these ballots
    are arranged in order of preference. This function returns only the first
    choice pick on each ballot.
    """
    >>> firstChoiceVotes(readBallot('data/simple.csv'))
    ['Aamir', 'Beth', 'Chris', 'Aamir']
    >>> firstChoiceVotes([['Abe', 'Betsy'], ['Eve'], ['Fred', 'Gina'], []])
    ['Abe', 'Eve', 'Fred']
    >>> firstChoiceVotes([['Bernard', 'Kamdem'], ['Yagami', 'Yuri'], ['Sonia', 'Keel']])
    ['Bernard', 'Yagami', 'Sonia']
    >>> firstChoiceVotes([['William', 'George'], ['Songo', 'Somo'], ['Khalil', 'King']])
    ['William', 'Songo', 'Khalil']

    """
    '''
    first_choice=[]
    for ballot in ballots:
        if ballot != []:
            first_choice.append(ballot[0])
        else:
            pass
    return first_choice

# Part 1.3
def mostVotes(votes):
    '''
    This function takes as input a list of strings of votes (e.g., the first
    choice of all voters as returned by firstChoice()), and returns a list of strings of names
     that appear the most number of times in votes.

    """
    >>> mostVotes(['Aamir', 'Beth', 'Chris', 'Aamir'])
    ['Aamir']
    >>> mostVotes(['Abe', 'Abe', 'Betsy', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida', 'Frida'])
    ['Abe', 'Betsy', 'Frida']
    >>> mostVotes([])
    []
    >>> mostVotes(['Bernard', 'Yagami', 'Sonia', 'Bernard', 'Yagami', 'Bernard', 'William'])
    ['Bernard']
    >>> mostVotes(['Playstation', 'Xbox', 'Wii', 'Playstation', 'Playstation', 'Playstation', 'William'])
    ['Playstation']


    '''
    result=[]
    max_so_far=0
    for person in votes:
        count=votes.count(person)
        if count>max_so_far:
            max_so_far=count
            result=[person]
        elif count==max_so_far:
            result.append(person)
            if result.count(person)>1:
                result.remove(person)
    return result





# Part 1.5
def candidates(ballots):
    '''
    the function candidates() in voting.py which takes a list of lists of
    strings (e.g., those returned by readBallot()) as input, and then creates
    and returns a new list of strings containing the names of all candidates
    that appear on any of the ballots, in the order that they appear

    >>> candidates(readBallot('data/simple.csv'))
    ['Aamir', 'Chris', 'Beth']
    >>> candidates([['Abe', 'Carmen'], ['Betsy'], ['Betsy', 'Gina'], []])
    ['Abe', 'Carmen', 'Betsy', 'Gina']
    >>> candidates([['Bernard', 'Yagami'], ['Yagami'], ['Rugal', 'Xavi']])
    ['Bernard', 'Yagami', 'Rugal', 'Xavi']
    >>> candidates([['Messi', 'Pedri'], ['Shakiri'], ['Pedri', 'Pedri']])
    ['Messi', 'Pedri', 'Shakiri']
    '''
    final_list=[]
    for ballot in ballots:
        for candidate in ballot:
            if candidate not in final_list:
                final_list.append(candidate)
    return final_list



# Part 2.1
def leastVotes(votes, candidates):
    ''' This function takes as input a list of strings of votes (e.g., the first
     choice of all voters), and returns a list of the names appearing the least number of
     times in the list votes. Along with the list of votes, it also takes the
     list of candidates involved so as to account for the fact that there might
     be no vote for a given candidate.

    >>> leastVotes(['Aamir', 'Beth', 'Chris', 'Aamir'], ['Aamir', 'Beth', 'Chris'])
    ['Beth', 'Chris']
    >>> leastVotes(['Abe', 'Abe', 'Betsy', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida', 'Frida'], ['Abe', 'Betsy', 'Carmen', 'Dave', 'Eva', 'Frida'])
    ['Carmen', 'Dave', 'Eva']
    >>> leastVotes(['Abe', 'Betsy', 'Betsy'], ['Abe', 'Betsy', 'Carmen'])
    ['Carmen']
    >>> leastVotes(['Kamdem', 'Khalil', 'Kamdem'], ['Bernard', 'Kamdem', 'Khalil'])
    ['Bernard']
    >>> leastVotes(['Khalil', 'Bernard', 'Kamdem'], ['Bernard', 'Kamdem', 'Khalil'])
    ['Bernard', 'Kamdem', 'Khalil']
    '''
    result=[]
    min_so_far=len(votes)
    for person in candidates:
        count=votes.count(person)
        if count<min_so_far:
            min_so_far=count
            result=[person]
        elif count==min_so_far:
            result.append(person)
    return result



# Part 2.2
def majority(votes):
    '''
    This function takes as input a list of strings votes
    (e.g., the first-choice of all voters), checks if there is a single
    candidate who wins the majority (i.e., more than half) of the votes, then
    returns the name of that candidate if such a candidate exists.

    >>> majority(['Aamir', 'Beth', 'Chris', 'Aamir'])

    >>> majority(['Abe', 'Abe', 'Abe', 'Betsy', 'Carmen', 'Dave', 'Abe', 'Abe', 'Frida'])
    'Abe'
    >>> majority(['Lionel', 'Nathan', 'Nathan', 'Nathan', 'Messi', 'Pedri', 'Nathan'])
    'Nathan'
    >>> majority(['Lionel', 'Pedri', 'Pedri', 'Songo', 'Kamdem', 'David', 'Pedri', 'Pedri', 'Pedri'])
    'Pedri'

    '''
    for person in votes:
        count=votes.count(person)
        if count>(len(votes)//2):
            return person


# Part 2.3
def eliminateCandidates(candidates, ballots):
    ''' Takes as inputs a list of strings representing value to be removed from the
    list of lists in ballots and returns the updated ballots as a new list of lists of strings.

    >>> eliminateCandidates(['Chris'], readBallot('data/simple.csv'))
    [['Aamir', 'Beth'], ['Beth', 'Aamir'], ['Beth', 'Aamir'], ['Aamir', 'Beth']]
    >>> eliminateCandidates(['Samwise Gamgee', 'Elizabeth Bennet'],readBallot('data/characters.csv')[0:3])
    [['Harry Potter', 'Scarlett OHara'], ['Harry Potter', 'Scarlett OHara'], ['Scarlett OHara', 'Harry Potter']]
    >>> eliminateCandidates(['Kamdem', 'Khalil'],[['Bernard', 'Khalil', 'Kamdem'], ['Khalil', 'Kamdem', 'Bernard']])
    [['Bernard'], ['Bernard']]
    >>> eliminateCandidates(['Bernard'],[['Bernard', 'Khalil', 'Kamdem'], ['Khalil', 'Kamdem', 'Bernard']])
    [['Khalil', 'Kamdem'], ['Khalil', 'Kamdem']]
    '''

    for ballot in ballots:
        for candidate in candidates:
            if candidate in ballot:
                ballot.remove(candidate)
    return ballots



if __name__ == '__main__':
    # this allows us to run the doctests included in the functions above
    # when the file is run as a script#
    from doctest import testmod  # this import is necessary when testing
    testmod(verbose=True)
