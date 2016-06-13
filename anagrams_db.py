from anagram_sets2 import *
import shelve


def store_anagrams(filename,h):
    """
    Stores anagrams in h in shelf

    filename: string file name of shelf
    ad: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word,word_list in h.items():
        shelf[word] = word_list

    shelf.close()

def read_anagrams(filename,word):
    """
    Reads anagrams from filename if key exists

    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []




h = all_anagrams('book.txt')
store_anagrams('anagrams.db', h)
