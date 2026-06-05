# Understand: Input a list and output the items in the list
# Plan: We should write a function that takes in a list and uses a for loop to go through all the items and print them on a new line
# Implement: Run a for loop and just print out each item using iterations

def print_list(lst):
    for x in range(len(lst)):
        print(lst[x])
lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)