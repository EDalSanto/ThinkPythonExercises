def make_word_dict():
    """Reads the words in words.txt and returns a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

def children(word,word_dict):
    """
    Returns list of all words that can be formed by removing one letter
    """
    t = []
    for char in word:
        new_w = word.replace(char,"")
        if new_w in word_dict:
            t.append(new_w)
    return t

"""
Memo is a dictionary that maps from each word that is know to be reducible to a list of its reducible children. It starts with the empty string.
"""
memo = {}
memo[""] = [""]

def is_reducible(word,word_dict):
    """
    If word is reducible, returns a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is reducible. The empty string is also reducible.

    word: string
    word_dict: dictionary with words as keys
    """
    # If we have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # Otherwise, check each of the children and make a list of the reducible ones
    res = []
    for child in children(word,word_dict):
        t = is_reducible(child,word_dict)
        if t:
            res.append(child)

    memo[word] = res
    return res

def all_reducible(word_dict):
    """
    Checks all words in the word_dict; returns a list of reducible ones.

    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t:
            res.append(word)
    return res

d = make_word_dict()
# print is_reducible('sprite',d)
x = all_reducible(d)
x.sort(key=lambda x: len(x),reverse=True)
print x[0:5] # Longest five
# Completeing is first
