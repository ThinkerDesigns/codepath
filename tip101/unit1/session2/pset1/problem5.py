# Understand: We want to find the biggest and smallest values and then take the difference
# Plan: We need to use the min & max functions in python to get these values from the list and then take their differences
# Implement: We can have a function to take the list and apply these built-in functions to them and then output the difference
def max_difference(lst):
    i = max(lst)
    j = min(lst)
    return i - j
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
