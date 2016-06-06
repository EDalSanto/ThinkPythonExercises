def histogram(s):
    """
    Returns histogram of string as dictionary

    s: string
    """
    d = {}
    for c in s:
        if c != " ":
            d[c] = d.get(c,0) + 1
    return d

print histogram('helllloo') == {'h': 1, 'e': 1, 'l': 4, 'o': 2}

h = histogram('parrot')

def print_hist(h):
    """
    Returns sorted histogram keys
    """
    return sorted(h.keys())

print print_hist(h) == ['a', 'o', 'p', 'r', 't']

def reverse_lookup(h,v):
    """
    Performs a reverse lookup for a key with a certain value

    h: dictionary
    v: value

    Returns a list of all keys with value, v
    """
    t = [ k for k in h if h[k] == v ]
    return t

print reverse_lookup(h,10) == []

def invert_dict(h):
    """
    Inverts dictionary

    h: a dictionary
    """
    inverse = {}
    for key in h:
        val = h[key]
        inverse.setdefault(val,[])
        inverse[val].append(key)
    return inverse

print invert_dict(h) == {1: ['a', 'p', 't', 'o'], 2: ['r']}

def has_duplicates(t):
    d = {}
    for elm in t:
        if elm in d:
            return True
        else:
            d[elm] = False
    return False

def has_duplicates2(t):
    """
    Utilized Set properties to check for duplicates
    """
    return len(set(t)) < len(t)


print has_duplicates2([1,2,2]) == True
