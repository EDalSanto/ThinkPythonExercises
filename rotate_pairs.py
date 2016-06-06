from dictVlist import *
from rotate import *

def rotate_pairs(word,word_dict,n):
    """
    Finds all words that can be created by rotating word n spaces

    word: string
    word_list: list of strings
    n: shifts

    Returns: # of words that can be created through rotation
    """
    rotations = 0
    for i in range(1,n):
        rotated = rotate_word(word,i)
        if rotated in word_dict:
            rotations += 1
    return rotations

# print rotate_pairs('he',d,26)

def find_greatest_rotator(word_dict,n):
    """
    Returns word that has greatest number of rotated words
    """
    rotate_best = None
    rotations = 0
    for word in word_dict:
        if rotate_pairs(word,word_dict,n) > rotations:
            rotate_best = word
            rotations = rotate_pairs(word,word_dict,n)
    return rotate_best, rotations

# print find_greatest_rotator(d,26) # 'he', 5
