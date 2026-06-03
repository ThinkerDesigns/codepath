# WIP - only finds the first negative and exits
def print_negatives(lst):
    i = 0
    while (i <= len(lst)):
        for x in range(len(lst)):
            if lst[x] > 0:
                continue
            elif lst[x] < 0:
                return(lst[x])
            i += 1
                
example = [3,-2,2,1,-5]
example2 = [1,2,3,4,5]
print(print_negatives(example))
#print(print_negatives(example2))