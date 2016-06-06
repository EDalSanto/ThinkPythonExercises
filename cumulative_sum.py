def cumulative_sum(list):
    """
    Takes a list of numbers and returns cumulative sum utilizing Python list comprehension

    list: list of numbers

    Return: sum of numbers in list
    """
    new_list = [ sum(list[:index+1]) for index,num in enumerate(list) ]
    return new_list

print cumulative_sum([1,2,3]) == [1,3,6]
