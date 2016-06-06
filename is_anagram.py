def is_anagram(word1,word2):
    """
    Find if two words are anagrams that is you can rearrange one to spell the other

    word1: string
    word2: string

    Return: True or False
    """
    s1 = sorted(list(word1))
    s2 = sorted(list(word2))
    return s1 == s2


print is_anagram('tom','mot') == True
print is_anagram('bob','tim') == False
