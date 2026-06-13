# WIP - 73.40 is coming out as a truncated 73.4
def convertTemp(celsius):
    ans = []
    ans.append(celsius + 273.15)
    ans.append((celsius*1.80)+32.00)
    return ans
temperatures = convertTemp(23.00)
print(temperatures)