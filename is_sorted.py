def is_sorted(t):
    """
    Takes a list t and returns whether or not it is sorted in ascending order

    t: list of elements that can be compared with relational operators

    Returns: True or False
    """
    for index,elm in enumerate(t[:-1]):
        if elm > t[index+1]:
            return False
    return True

print is_sorted([1,2,3]) == True
print is_sorted(['b','a']) == False
