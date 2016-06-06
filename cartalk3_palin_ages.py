# Digits have been reversible 6 times so far
# Would happen again in a few years
# And one more time if really lucky making it a total of 8
# Range of 0-100, 8 occurences of this palindromic event


def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]

def check():
    """
    According to Puzzler scenario, finds current age of daughter that satisfies condition of having 8 palindromic ages with her mother throughout her life
    """
    for i in range(18,70): #Enumerating different possible reasonable ages mother could have given birth
        daughter = 0
        palin_ages = [] # Age of Daughter when palindromic age occurred
        for j in range(i,100): # Simulating aging of mother and daughter from a given mother starting age, i
            mother = j
            if are_reversed(daughter,mother):
                palin_ages.append(daughter)
                if len(palin_ages) == 8:
                    return "Current age of daughter: %d" % palin_ages[5]
            daughter += 1

# print check()
# Current age of daughter: 57
