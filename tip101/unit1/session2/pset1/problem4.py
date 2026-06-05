# Understand: We want a lst that has every single item of the original list negated
# Plan: We will use a funciton that has a for loop that goes through and negate every item and appends it to a new list
# Implement: We will take the original lst, iterate through every item and negate it, and finally append it to a new list. Then we will output the new list
def flip_sign(lst):
    result = []
    for x in range(len(lst)):
        i = lst[x] * -1
        result.append(i)
    return result
lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)