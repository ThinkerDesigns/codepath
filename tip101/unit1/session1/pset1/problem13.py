def sum_positive_range(stop):
    i = 0
    for x in range(1,stop + 1):
        i +=x
    return(i)
sum = sum_positive_range(6)
print(sum)