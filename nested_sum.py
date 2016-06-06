def nested_sum(list):
    sum = 0
    for elm in list:
        if type(elm) == int:
            sum += elm
        else:
            temp = nested_sum(elm)
            sum += temp
    return sum

# print nested_sum([1,2,3,[3,4,[4,3]]]) == 20 # True
