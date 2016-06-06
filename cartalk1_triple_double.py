fin = open("ThinkPython/words.txt")

def triple_double(word):
    """Tests if a word contains three consecutive double letters"""
    i = 0
    doubles = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            doubles += 1
            if doubles == 3:
                return True
            i += 2
        else:
            doubles = 0
            i += 1
    return False

def find_triple_double():
    """Reads a word list and prints words with triple double letters"""
    for line in fin:
        word = line.strip()
        if triple_double(word):
            print word
