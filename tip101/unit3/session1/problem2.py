# Understand: Wants to take a string and swap the first and last characters
# Plan: Store the first and last characters into their own variables then swap
# Implement: Return the last + middle + first parts of the string
def swap_ends(my_str):
    first = my_str[0]
    last = my_str[-1]
    middle = my_str[1:len(my_str) - 1]
    return(last + middle + first)
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)