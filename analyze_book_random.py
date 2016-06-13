import random
from analyze_book import *
from bisect import bisect

def random_word(h):
    """
    Chooses a random word from a histogram

    The probability of each word is proportional to its frequency

    This could be made faster by computing the cumulative frequencies once and reusing them
    """
    # Creates lists of Words and Cumulative sum of words in book
    words = []
    freqs = []
    total_freq = 0
    for word,freq in h.items():
        total_freq += freq
        freqs.append(total_freq)
        words.append(word)

    # Chooses a random value and finds its location in cumulative list
    num = random.randint(1,total_freq)
    index = bisect(freqs, num)
    # Bisect returns index value of where num would be in land in list freqs
    # Returns word at index
    return words[index]

# h = process_file("book.txt")
# print random_word(h)
