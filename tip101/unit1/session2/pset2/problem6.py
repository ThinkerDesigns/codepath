def reverse_list(lst):
    result = []
    for x in range(len(lst)):
        result.append(lst[len(lst) - (x+1)])
    return result
lst = [1,2,3,4,5]
rev_lst = reverse_list(lst)
print(rev_lst)