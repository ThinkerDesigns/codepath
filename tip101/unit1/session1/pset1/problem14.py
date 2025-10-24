def sum_range(start,stop):
    i = 0
    for x in range(start, stop + 1):
        i += x
    return(i)
sum = sum_range(3,9)
print(sum)