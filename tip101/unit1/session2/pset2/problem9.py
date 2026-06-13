def list_to_number(digits):
    result = ""
    for x in range(len(digits)):
        result = result + str(digits[x])
    return result
digits = [1,0,3]
number = list_to_number(digits)
print(number)