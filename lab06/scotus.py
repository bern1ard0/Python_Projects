# Support function for analyzing the decisions of the Supreme Court.
# Much of this work follows that of Fowler (see paper directory).

# STUDENTS: add code at places marked "pass",
#           and Remove pass-es before submitting.
"""
This module provides a number of methods that support the analysis of
Supreme Court of the United States (SCOTUS) decisions.

It provides three important functions:
   readDecisions - read yearly dockets of cases and their citation counts
   hIndex - given a list of citation counts, compute the 'h-index'
   plotImpacts - plot the h-index for each year's docket of cases
   readCourts - assembles a dictionary that maps the name of a justice to a 
                tuple of case citations
    byImpact - a 'key function' for use for sorting tuples by citation count
    rankJustices - constructs a list of (justice, hIndex) pairs sorted in 
                    decreasing order of hIndex
"""
import csv
import matplotlib.pyplot as plt

def readDecisions(filename):
    """
    This function takes the name of a CSV file (string) containing Supreme Court
    data and creates a dictionary that maps a year (int) to that year's docket
    (a tuple of case citation counts).

    >>> len(readDecisions('data/judicial.csv'))
    235
    >>> db = readDecisions('data/judicial.csv')
    >>> (min(db), max(db))  # range of dates for decisions
    (1754, 2002)
    >>> max(readDecisions('data/judicial.csv'))
    2002
    >>> readDecisions('data/judicial.csv')[1793]
    (0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 31, 0, 0, 0, 0, 0)
    >>> [ year in db for year in [ 1753, 1754, 1755 ] ]
    [False, True, False]
    >>> len(db[2002])
    17
    >>> len(db[1760])
    2
    >>> db[1760]
    (0, 0)
    """
    # a dictionary that maps a year (key) to a tuple of citation counts (indeg)
    db = dict()
    tp= tuple()
    with open(filename) as caseFile:
        for row in csv.reader(caseFile):
            # ignore the top header line in caseFile
            # Hint: what is different about the data in the header row?
            if row[0]!="caseid":
            # extract relevant info in each row (year, indeg)
                year=int(row[3])
                indeg=int(row[8])

            # update your dictionary (db)
            # Hint: remember that you can concatenate tuples
                if year in db:
                    tp=tp+(indeg,)
                    db[year]=tp
                elif year not in db:
                    tp=tuple()
                    tp=tp+(indeg,)
                    db[year]=tp
            
    # return the accumulated data
    return db

def hIndex(citations):
    """Computes and returns the h-index (int) of citations (tuple of citation counts).

    >>> hIndex( (0, 2, 15, 9, 7, 48, 4, 82, 14, 6) )
    6
    >>> hIndex( (2, 2, 2, 2) )
    2
    >>> hIndex( (5, 4, 3, 2, 1) )
    3
    >>> hIndex( (0, 0) )
    0
    >>> hIndex( (3, 3, 3, 3) )
    3
    >>> hIndex( (7, 6, 5, 4, 3, 2, 1) )
    4
    """
    sorted_citation=sorted(citations,reverse=True) #citation sorted in descending order
    index=range(len(sorted_citation))    #list of indices of sorted citation
    for n in index:                      
        if n>=int(sorted_citation[n]):   #finding index which is greater than 
            return n




def plotImpacts(dockets, plotFilename):
    """Generate a line plot of the h-index associated with each year in
    the database, dockets (dictionary).  Plot saved as file with name found in
    plotFilename (string).
    """
    # 1. extract all the years into a list, sorted into increasing order.
    years=sorted(dockets.keys())

    # 2. compute a list of hIndex values for each year's case citations
    impacts=[ hIndex(dockets[year]) for year in years]

    # 3. generate the plot (see lab handout)
    plt.title('Plot Impacts')
    plt.xlabel('Years')
    plt.ylabel('hIndex')
    plt.plot(years, impacts, 'b-')
    plt.savefig(plotFilename)

def readCourts(justiceFilename,dockets):
    """Given a justiceFilename (string) a path to csv file of Chief Justices and
    their terms (name, start-year, end-year) and a database of case citation
    counts called dockets (dict), assemble and return a dictionary that maps the name
    of a justice to a tuple of case citations.

    >>> len(readCourts('data/chiefJustices.csv', readDecisions('data/judicial.csv')))
    16
    >>> db = readDecisions('data/judicial.csv')
    >>> cjdb = readCourts('data/chiefJustices.csv', db)
    >>> cjdb['John Rutledge'] == db[1795]
    True
    >>> cjdb['John Marshall'] == db[1835]
    False
    >>> cjdb['William Rehnquist'] == db[2002]
    False
    >>> cjdb['John Rutledge'] == db[1795]
    True
    """
    cjd = dict()
    
    
    with open(justiceFilename) as f:
        # parse rows
        header=f.readline()   #ignoring the header line
        for row in csv.reader(f):    #iterating over list of justicefilename
            tp= tuple()
            jname=row[0]             #assigning justice name to 0th index in row
            startyr=int(row[1])      #start year is the integer value of 1st index in row
            endyr=int(row[2])        #end year is the integer value of 2nd index in row
            for year in range(startyr,endyr+1):  #iterating through range of start year and end year.
                tp= tp + dockets.get(year, ())  #adding the tuple corresponding to the correct year
                cjd[jname]=tp        # NB: in case a year is absent, the .get method sets a default value in place. 
    
    return cjd

def byImpact(pair):
    """A 'key function' for use in sorted.

    >>> byImpact( ('John Jay', 5 ) )
    5
    """
    name, impact = pair
    return impact

def rankJustices(cjdb):
    """Construct a list of (justice, hIndex) pairs sorted in decreasing order
    of hIndex given cjdb (dict).

    >>> db = readDecisions('data/judicial.csv')
    >>> cjdb = readCourts('data/chiefJustices.csv', db)
    >>> rankJustices(cjdb)[-2]
    ('John Jay', 5)
    >>> rankJustices(cjdb)[0]
    ('Earl Warren', 62)
    >>> rankJustices(cjdb)[10]
    ('John Marshall', 28)
    """
    justiceIndex=[] 
    cjdblist=list(cjdb.items()) #changing dictionary items into a list of tuples (justice_name, citation)
    for nameCitation in cjdblist: #iterating through each tuple in list
        jindex=hIndex(nameCitation[1])    #finding the hindex of each citation
        (jname, index)= (nameCitation[0], jindex) #creating a tuple(justice_name, hindex of citation)
        justiceIndex.append((jname, index)) #appending tuples to empty list justiceIndex
    final_list=sorted(justiceIndex, key=byImpact, reverse=True)#sorting the tuples with byImapact function as key
    return final_list
   
def test():
    """Exercise document tests."""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()  # check to make sure methods are correct

    # 1. read in decisions
    db = readDecisions('data/judicial.csv')

    # 2. plot their impacts
    plotImpacts(db, 'scotusImpact.pdf')

    # 3. Read in the court impacts
    courtDB = readCourts('data/chiefJustices.csv',db)

    # 4. Build rankings
    ranking = rankJustices(courtDB)

    # 5. Print the rankings out
    for court, impact in ranking:
        print("{}: {}".format(court,impact))
