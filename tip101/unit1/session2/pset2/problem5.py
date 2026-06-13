def find_missing(nums):
    nums = sorted(nums)
    i = 0
    for x in range(i,max(nums)):
        if nums[x] == i:
            i = i + 1
            continue
        else:
            return nums.index(nums[x])

nums = [2,4,1,0,5]
missing_num = find_missing(nums)
print(missing_num)