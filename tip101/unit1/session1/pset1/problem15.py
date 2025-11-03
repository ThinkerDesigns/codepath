# WIP - can't print None for list with no negatives
def print_negatives(lst):
    i = 0
    for x in range(len(lst)):
        if lst[x] < 0:
            print(lst[x])
            i +=1
        elif lst[x] > 0:
            continue
                
example = [3,-2,2,1,-5]
example2 = [1,2,3,4,5]
print_negatives(example)
print_negatives(example2)