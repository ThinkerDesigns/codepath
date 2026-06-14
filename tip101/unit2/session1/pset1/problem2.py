def create_dictionary(keys, values):
    result = {}
    for x in range(len(keys)):
        result[keys[x]] = values[x]
    return result
keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys,values))