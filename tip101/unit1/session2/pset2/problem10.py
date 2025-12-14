def move_zeroes(nums):
    result = []
    for x in range(len(nums)):
        if nums[x] != 0:
            result.append(nums[x])
    if len(result) != len(nums):
        for x in range(len(nums) - len(result)):
            result.append(0)
    return result
nums = [1,0,2,3,0,0,4]
new_nums = move_zeroes(nums)
print(new_nums)