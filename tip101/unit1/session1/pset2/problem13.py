def sqaures(nums):
    for x in range(len(nums)):
        nums[x] = nums[x] * nums[x]
    return nums
print(sqaures([1,2,3,4]))