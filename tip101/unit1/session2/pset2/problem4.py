def check_num(lst, num):
    if num in lst:
        return True
    else:
        return False
lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)