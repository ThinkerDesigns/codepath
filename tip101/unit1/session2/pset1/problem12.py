def linear_search(lst, target):
    i = 0
    for x in range(len(lst)):
        if target not in lst:
            return -1
        elif lst[x] != target:
            i = i + 1
        elif lst[x] == target:
            return i
lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)
lst = [1,4,5,2,8]
position = linear_search(lst,10)
print(position)