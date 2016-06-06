wlist = open("words.txt")
from b import *
from wordlist import *
import time

def make_dict(wordlist):
    d = {}
    for line in wordlist:
        word = line.strip()
        d[word] = 1
    return d

d = make_dict(wlist)

# Test for how long search with in operator and dict
start_time = time.time()
print 'the' in d
elapsed_time = time.time() - start_time
print elapsed_time # 3.69548797607e-05

# '' in operator and list
t = make_word_list1()
start_time = time.time()
print 'the' in t
elapsed_time = time.time() - start_time
print elapsed_time # 0.00230121612549

# '' bisection search and list
start_time = time.time()
b(t,'the')
elapsed_time = time.time() - start_time
print elapsed_time # 1.50203704834e-05
