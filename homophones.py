from pronounce import read_dictionary

def make_word_dict():
    """Read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d


def homophone(word1,word2,phonetic):
    """
    Checks if two words can be pronounced the same way

    word1,word2: strings
    phonetic: map from words to pronunciation codes
    """
    if word1 not in phonetic or word2 not in phonetic:
        return False
    return phonetic[word1] == phonetic[word2]

def check_word(word,word_dict,phonetic):
    """
    Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.

    word: string
    word_dict: dictionary with words as keys
    phonetic: map from words to pronunciation codes
    """
    no_first = word[1:]
    no_second = word[0] + word[2:]
    if no_first not in word_dict or no_second not in word_dict:
        return False
    elif homophone(word,no_first,phonetic) and homophone(word,no_second,phonetic):
        return True

d = make_word_dict()
phonetic = read_dictionary()

# print check_word('hello',d,phonetic) == False
# print check_word('scent',d,phonetic) == True
# for word in d:
#     if check_word(word,d,phonetic):
#         print word
# llama
# llamas
# scent
