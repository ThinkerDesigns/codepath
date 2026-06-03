def power(base,exponent):
    i = 1
    result = 1
    while i <= exponent:
        result = result * base
        i += 1
    return result
print(power(2,5))
print(power(3,3))