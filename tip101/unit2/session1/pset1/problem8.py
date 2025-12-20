def index_to_value_map(lst):
    result = {}
    for x in range(len(lst)):
        result[x] = lst[x]
    return result
lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))