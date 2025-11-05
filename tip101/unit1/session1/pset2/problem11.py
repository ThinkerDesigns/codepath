def list_length(lst):
    i = 0
    for x in lst:
        i += 1
    return i
lst = [2,4,6,8,10]
length = list_length(lst)
print(length)