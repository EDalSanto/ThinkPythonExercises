
def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def most_frequent(s):
    """
    Returns letters of string in reverse order of frequency
    """
    hist = make_histogram(s)

    t = []
    for l,freq in hist.iteritems():
        t.append((freq,l))

    t.sort(reverse=True)

    # res = []
    # for freq,l in t:
    #     res.append(l)

    return t

def read_file(file):
    """
    Reads the contents of a file as a string
    """
    return open(file).read()

s = read_file("words.txt")
t = most_frequent(s)
for x in t:
    print x
