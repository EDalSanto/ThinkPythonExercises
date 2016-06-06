def rotate_letter(letter,n):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start

    return chr(i)

def rotate_word(word,n):
    return "".join([ rotate_letter(char,n) for char in word ])

print rotate_word('melon',-10)
# cubed
