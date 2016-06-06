def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print middle('hi')

def is_palin(word):
    if len(word) < 2:
        return True
    elif first(word) == last(word):
        return is_palin(middle(word))
    return False
