def get_last(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[len(lst) - 1]
example = [3,1,6,7,5]
print(get_last(example))