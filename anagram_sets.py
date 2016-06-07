def signature(s):
    """
    Returns the signature of this string, which is a string that contains all of the letters order
    """
    t = list(s)
    t.sort()
    t = "".join(t)
    return t

def all_anagrams(filename):
    """
    Finds all anagrams in a list of words

    filename: string filename of the word list

    Returns: a map from each word to a list of its anagrams
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        s = signature(word)

        if s not in d:
            d[s] = [word]
        else:
            d[s].append(word)
    return d

def print_descending_anagrams():
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v),v))

    t.sort(reverse=True) # Sort in descending order

    for x in t:
        print x

def filter(l,d):
    """
    Finds all keys of length l in a dictionary d

    d: dictionary mapping from word to list of anagrams
    l: integer numbers of letters

    Returns list of tuples that satisfy conditions
    """
    t = []
    for k in d.keys():
        if len(k) == l and len(d[k]) > 1:
            t.append((k,d[k]))
    t.sort(key=lambda x: len(x[1]),reverse=True)
    # Sorted in descending order
    return t


d = all_anagrams("words.txt") # Creates dict of mapping from word to list of anagrams
print filter(8,d) # Returns all 8 letter words in dict
