import string

def process_file(filename):
    """
    Traverses a text file and creates dict of word occurences. Removes all punctuation, whitespace, and uppercase

    filename: book as text file

    Returns: word frequency dict
    """
    d = {}
    for line in open(filename):
        words = line.split()
        for word in words:
            s = word.strip(string.punctuation).strip(string.whitespace).lower()
            d[s] = d.get(s,0) + 1
    return d

def total_words(filename):
    """
    Returns total number of words(keys) in file
    """
    return len(process_file(filename))

def twenty_most_frequent(filename):
    """
    Returns 20 most common words in filename

    filename: book saved as text file
    """
    d = process_file(filename)
    d = sorted(d.items(),key=lambda x: x[1],reverse=True)
    return d[:20]

# print twenty_most_frequent("book.txt")
