def count_less_than(numbers, threshold):
    i = 0
    for x in range(len(numbers)):
        if numbers[x] < threshold:
            i += 1
    return i
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)