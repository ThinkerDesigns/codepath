def find_divisors(n):
    result = []
    i = n
    for x in range(n):
        if n % i == 0:
            result.append(i)
            i = i - 1
        elif n % i != 0:
            i = i - 1
    result = sorted(result)
    return result
lst = find_divisors(6)
print(lst)