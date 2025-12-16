def find_all_occurrences(lst, target):
    result = []
    i = 0
    for x in range(len(lst)):
        if lst[x] == target:
            result.append(i) # lst.index(lst[x]) doesnt work in this case since multiple indexes have the same value so it will just fill the first index it finds for all the values in the new list
            i = i + 1
        else:
            i = i + 1
            continue
    return result
lst = [1,2,6,5,2,1,3,2,2]
index_list = find_all_occurrences(lst, 2)
print(index_list)