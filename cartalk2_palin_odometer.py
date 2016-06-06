def has_palindrome(i,start,length):
    """return True if the integer i, when written as a string, contains a palindrome with length(len), starting at index(start).
    """
    s = str(i)[start:start+length]
    return s == s[::-1]

# print has_palindrome(345,1,2) == False
# print has_palindrome(3455,2,2) == True
# #

## Requiremnts of Puzzler
# Started: last 4 digits palindormic
# +1 mile: last 5
# +1 mile: middle 4
# +1 mile: all 6
# What was on the odometer when first looking?(Start)

def check(i):
    """
    Check whether an integer (i) has the properties described in the puzzler
    """
    return (has_palindrome(i,2,4) and
            has_palindrome(i+1,1,5) and
            has_palindrome(i+2,1,4) and
            has_palindrome(i+3,0,6))

def check_all():
    """
    Enumerate all six-digit numbers and print any that satisfy requirements of puzzler above
    """
    for i in xrange(100000,1000000): # Iterate through all combinations of 6 numbers
        if check(i):
            print i

# print 'The following are the possible odometer readings:'
# check_all()
# print
# 198888
# 199999
