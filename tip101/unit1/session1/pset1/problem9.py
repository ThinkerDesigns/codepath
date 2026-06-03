def get_first(lst):
    if len(lst) == 0:
        return None
    else:
        return lst[0]
example = [3,1,6,7,5]
print(get_first(example))