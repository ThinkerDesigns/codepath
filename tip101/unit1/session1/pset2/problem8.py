def above_threshold(lst, threshold):
    result = []
    for x in range(len(lst)):
        if lst[x] > threshold:
            result.append(lst[x])
    return result
lst = [8,2,13,11,4,10,14]
result = above_threshold(lst, 10)
print(result)