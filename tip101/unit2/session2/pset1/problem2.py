'''
Write a function that takes in two dictionaries, dict1 and dict2 and finds all keys common to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
	pass
Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
Example Output:

['b', 'c']
'''
# Understand: The function would like to compare the dictionaries and see the similarites
# Plan: create a new list to return, iterate through both dicts and add the common keys to the list 
# Edge cases: dicts different lengths, empty dict
# Implement: Check if they key is in the first dict and if not move on

def common_keys(dict1,dict2):
    result = []
    for key in dict1:
        if key in dict2:
            result.append(key)
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)
