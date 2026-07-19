def is_monotonic(nums):
    higher = 0
    lower = 0
    for x in range(len(nums) - 1):
        if (nums[x] <= nums[x+1]):
            higher += 1
        elif (nums[x] >= nums[x+1]):
            lower += 1
    if (higher == (len(nums) -1)) or (lower == (len(nums)-1)):
        return True
    return False
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))