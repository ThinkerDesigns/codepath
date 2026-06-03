def multiply_list(lst, multiplier):
    for x in range(len(lst)):
        lst[x] = lst[x] * multiplier
    return lst
lst = [1,2,3]
new_lst = multiply_list(lst, 3)
print(new_lst)