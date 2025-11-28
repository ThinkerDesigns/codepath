def get_evens(lst):
    result = []
    for x in range(len(lst)):
        if lst[x] % 2 == 0:
            result.append(lst[x])
    return result
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)