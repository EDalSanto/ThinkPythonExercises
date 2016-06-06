from bisect import bisect_left

def b(t,word):
	"""
	Checks whether a word is in a list and where

	Precondition: the words in the list are sorted_t

	t: list of strings
	word: strings

	Returns: True or False
	"""
	i = bisect_left(t, word)
	if i != len(t) and t[i] == word:
		return True
	return False

print b([1,2,3],2) == True
