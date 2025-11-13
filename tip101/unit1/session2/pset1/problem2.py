# Understand: Input a list and output the items in the list
# Plan: We should write a function that takes in a list and uses a for loop to go through all the items, double them, and print them on a new line
# Implement: Run a for loop, double each item, and just print out each doubled item using iterations
def doubled(lst):
    for x in range(len(lst)):
        print(lst[x] * 2)
lst = [1,2,3]
doubled(lst)