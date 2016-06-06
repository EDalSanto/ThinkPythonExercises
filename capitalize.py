def capitalize_all(t):
    """
    Capitalizes all strings in a list

    t: a list of strings

    Returns new list with all strings capitalized
    """
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

print capitalize_all(['hello']) == ['Hello']
print capitalize_all(['hello','goodbye']) == ['Hello', 'Goodbye']

def capitalize_nested(nested_list):
    """
    Takes nested list of strings and turns into a new nested list all strings capitlized

    nested_list: list of strings and nested string lists

    Returns: New nested list with all strings capitlized
    """
    new_list = []
    for elm in nested_list:
        if type(elm) == str:
            new_list.append(elm.capitalize())
        else:
            new_list.append(capitalize_all(elm))
    return new_list

nested_list = ['hello','goodbye',['johnbob','sir']]
print capitalize_nested(nested_list) == ['Hello','Goodbye',['Johnbob','Sir']]
