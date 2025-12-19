def keys_v_values(dictionary):
    keys = 0
    values = 0
    for x in range(len(dictionary)):
        keys = keys + list(dictionary)[x]
        values = values + list(dictionary.values())[x]
    if keys > values:
        return "keys"
    else:
        return "values"
dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)