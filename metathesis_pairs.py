# Metathesis words are a special case of anagrams where only two letters can be swapped

from anagram_sets import *

def metathesis_pairs(d):
    """
    Loops through all anagram lists of same length and finds words that differ by exactly 2

    d: dictionary of mapping of words to anagrams

    prints Metathesis pairs
    """
    for anagrams in d.itervalues():
        for word1 in anagrams:
            for word2 in anagrams[1:]:
                if word_distance(word1,word2) == 2:
                    print word1, word2

def word_distance(word1,word2):
    """
    Computes the number of differences between two words.

    word1,word2: strings

    Returns integer
    """
    assert len(word1) == len(word2)
    # Won't work/run if word lengths are different
    # Perhaps could be handled by adding diff in lengths to diffs?

    diffs = 0
    for c1,c2 in zip(word1,word2):
        if c1 != c2:
            diffs += 1
    return diffs

# d = all_anagrams("words.txt")
# print metathesis_pairs(d)
