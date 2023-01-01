# Implements different voting rules

# import functions from voting module
from voting import *

# Part 1.4
def plurality(ballots):
    '''Takes as input ballot data as a list of lists of strings, and
    returns a list of strings of names of candidates who get the most votes.
    >>> plurality(readBallot('data/simple.csv'))
    ['Aamir']
    >>> plurality(readBallot('data/example.csv'))
    ['Ava']
    >>> plurality(readBallot('data/characters.csv'))
    ['Samwise Gamgee', 'Scarlett OHara']
    >>> plurality([['Bernard','Kamdem'],['Kamdem','Bernard'],['Kamdem','Bernard'],['Kamdem','Bernard']])
    ['Kamdem']
    '''
    firt_pick=firstChoiceVotes(ballots)
    winner=mostVotes(firt_pick)
    return winner


# Part 1.6
def bordaScore(candidate,ballots):

    '''
    This function takes as inputs a string and a list of lists and returns an
    integer value representing the score got by the string value using the borda
    count method.

    >>> bordaScore('Ava',readBallot('data/example.csv'))
    37
    >>> bordaScore('Bob',readBallot('data/example.csv'))
    42
    >>> bordaScore('Cid',readBallot('data/example.csv'))
    47
    >>> bordaScore('Bernard',[['Bernard','Kamdem'],['Kamdem','Bernard']])
    3
    >>> bordaScore('Kamdem',[['Bernard','Kamdem'],['Kamdem','Bernard'],['Kamdem','Bernard'],['Kamdem','Bernard']])
    7



    '''
    count=0
    points=0
    for ballot in ballots:
            points+=len(ballot)-ballot.index(candidate)
    return points

def borda(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns a list of strings of the names of candidates with the
    maximum borda score.

    >>> borda(readBallot('data/simple.csv'))
    ['Aamir']
    >>> borda(readBallot('data/example.csv'))
    ['Cid']
    >>> borda(readBallot('data/characters.csv'))
    ['Harry Potter']
    >>> borda([['Bernard','Kamdem'],['Kamdem','Bernard']])
    ['Kamdem', 'Bernard']
    >>> borda([['Bernard','Kamdem'],['Kamdem','Bernard'],['Kamdem','Bernard'],['Kamdem','Bernard']])
    ['Kamdem']
    '''
    max_so_far=0
    winner=[]
    for ballot in ballots:
        for candidate in ballot:
            candidatepoint=bordaScore(candidate,ballots)
            if candidatepoint>max_so_far:
                max_so_far=candidatepoint
                winner=[candidate]
            elif max_so_far==candidatepoint:
                winner.append(candidate)
                if winner.count(candidate)>1:
                    winner.remove(candidate)
    return winner



# Part 2.4
def rankedChoice(ballots):
    '''Takes as input ballot data as list of lists of strings, and
    returns the winner of the election based on ranked-choice
    voting as a list of strings of names.

    >>> rankedChoice(readBallot('data/simple.csv'))
    ['Aamir']
    >>> rankedChoice(readBallot('data/example.csv'))
    ['Bob']
    >>> rankedChoice(readBallot('data/characters.csv'))
    ['Scarlett OHara']
    >>> rankedChoice([['Abe', 'Betsy', 'Carmen'], ['Betsy', 'Abe', 'Carmen'], ['Carmen', 'Abe', 'Betsy']])
    ['Abe', 'Betsy', 'Carmen']
    >>> rankedChoice([['Sierra', 'Tao', 'Una'], ['Sierra', 'Tao', 'Una'], ['Tao', 'Sierra', 'Una'], ['Tao', 'Sierra', 'Una']])
    ['Sierra', 'Tao']
    '''
    result=[]
    result2=[]
    while True:
        for ballot in ballots:
            for person in ballot:
                if person==majority(ballot):
                    return result.append(person)

        n=len(candidates(ballots))
        for ballot in ballots:
            if len(leastVotes(ballot,candidates(ballots)))==n:
                return result2.append(candidates(ballots))


        for ballot in ballots:
            for person in ballot:
                if person in leastVotes(ballot,candidates(ballots)):
                    ballot.remove(person)






# Part 2.5
def condorcet(ballots):
    '''EXTRA CREDIT: Takes as input ballot data as list of
    lists of strings, and returns the winner of the election
    as a string (or empty string if there is no winner).
    '''
    pass

if __name__ == '__main__':
    from doctest import *
    testmod()

    # # Read in our ice cream ballots and run our election algorithms for Part 1.
    print('Ice-cream flavor class election results:')
    print('Plurality winner:', ", ".join(plurality(readBallot('data/icecream.csv'))))
    print('Borda winner:', ", ".join(borda(readBallot('data/icecream.csv'))))

    # # Read in our ice cream ballots and run our election algorithms for Part 2.
    print('Ranked-choice winner:', ", ".join(rankedChoice(readBallot('data/icecream.csv'))))

    # # Uncomment the following line if you complete the extra credit
    # print('Condorcet winner:', condorcet(readBallot('data/icecream.csv')))
