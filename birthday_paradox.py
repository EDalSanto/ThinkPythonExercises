def has_duplicates(t):
    """
    Takes a list and checks if any element appears more than once. Does not modify list

    t: list

    Return: True or False
    """
    for elm in t:
        if t.count(elm) > 1:
            return True
    return False

print has_duplicates([1,2,2]) == True
print has_duplicates([1,2]) == False

import random

def random_bdays(n):
    """
    Returns list of random integers between 1 and 365 that represent birthdays
    """
    birthdays = [ random.randint(1,356) for i in range(n) ]
    return birthdays

def birthday(n,simulations):
    """
    What are the chances that in a room of n people two share the same birthday

    n: number of people
    simulations: number of simulations

    Return: probablity as # of occurences with duplicates over total
    """
    duplicates = 0.0
    for sim in range(simulations):
        birthdays = random_bdays(n)
        if has_duplicates(birthdays):
            duplicates += 1
    return duplicates

num_students = 23
num_simulations = 1000

duplicates = birthday(num_students, num_simulations)

print 'After %d simulations' % num_simulations
print 'with %d students' % num_students
print 'there were %d simulations with at least one match' % duplicates
print "which means about %d percent of the time" % (duplicates/num_simulations*100)
