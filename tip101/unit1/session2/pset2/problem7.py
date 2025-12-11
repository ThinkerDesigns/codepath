def get_odds(nums):
    result = []
    for x in range(len(nums)):
        if nums[x] % 2 != 0:
            result.append(nums[x])
    return result
nums = [2,5,1,8,6,5]
odd_nums = get_odds(nums)
print(odd_nums)