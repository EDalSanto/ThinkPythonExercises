from wordlist import *
from b import *

word_list = make_word_list1()

def interlock(word_list,word):
    """
    Determine if a word is formed from alternating letters of    two words

    word_list: list of strings
    word: strings

    Returns: True or False
    """
    evens = word[::2]
    odds = word[1::2]
    return b(word_list,evens) and b(word_list,odds)

print interlock(word_list,'schooled') == True

def interlock_general(word_list,word,n=3):
    """
    Determine if a given word can be formed from n interleaved words

    n: number of interleaved words

    Returns: True or False
    """
    for i in range(n):
        inter = word[i::n]
        if not b(word_list,inter):
            return False
    return True


if __name__ == '__main__':
    word_list = make_word_list1()

    for word in word_list:
        if interlock(word_list, word):
            print word, word[::2], word[1::2]

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print word, word[0::3], word[1::3], word[2::3]
