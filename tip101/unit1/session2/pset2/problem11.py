def print_odd_indices(nums):
    for x in range(len(nums)):
        if nums.index(nums[x]) % 2 != 0:
            print(nums[x])
nums = [3,4,8,1,5,2]
print_odd_indices(nums)