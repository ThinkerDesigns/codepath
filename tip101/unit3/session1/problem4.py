# Understand: Wants the string to be reversed
# Plan: use a for loop, start at the end, and concat

def reverse_string(my_str):
    #return my_str[::-1]
    result = ""
    for character in range(len(my_str) - 1,-1,-1):
        result = result + my_str[character]
    return result
my_str = "live"
print(reverse_string(my_str))