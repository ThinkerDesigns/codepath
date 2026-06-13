def increment_values(lst):
    for x in range(len(lst)):
        lst[x] = lst[x] + 1
    return lst
lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)