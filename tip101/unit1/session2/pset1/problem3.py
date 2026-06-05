# Understand: We want a lst that has every single item of the original list doubled
# Plan: We will use a funciton that has a for loop that goes through and doubles every item and appends it to a new list
# Implement: We will take the original lst, iterate through every item and double it, and finally append it to a new list. Then we will output the new list
def doubled(lst):
    result = []
    for x in range(len(lst)):
        i = lst[x] * 2
        result.append(i)
    return result
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)