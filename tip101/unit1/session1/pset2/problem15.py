def count_evens(lst):
    i = 0
    for x in range(len(lst)):
        if lst[x] == 0:
            continue
        elif lst[x] % 2 == 0:
            i += 1
        elif lst[x] % 2 == 1:
            continue
    return i
lst1 = [1,5,7,9]
count1 = count_evens(lst1)
print(count1)

lst2 = [2,4,6,8]
count2 = count_evens(lst2)
print(count2)