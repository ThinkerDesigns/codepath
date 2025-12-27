'''
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

def sort_array_by_parity(nums):
    pass
Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
Example Output:

[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
[0]
'''
# undestand: have a list of all evens then odds
# input: list
# output: list
# edge cases: empty list, single element list
def sort_array_by_parity(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return nums
    left = 0
    right = len(nums) - 1
    temp = 0
    while (left < right):
        if (nums[left] % 2 == 0) and (nums[right] % 2 == 0):
            left += 1
            right -= 1
        elif (nums[left] % 2 != 0) and (nums[right] % 2 != 0):
            left += 1
            right -= 1
        elif (nums[left] % 2 != 0) and (nums[right] % 2 == 0):
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1
        elif (nums[left] % 2 == 0) and (nums[right] % 2 != 0):
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
            right -= 1
    return nums
#nums = [3,1,2,4]
nums = [2,3,6,1,5,4,64,17]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))