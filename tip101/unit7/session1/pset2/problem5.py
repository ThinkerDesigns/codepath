def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  # Base case: target not found within bounds

		# find middle index of list
    mid = (left + right) // 2
    
    # If the middle element is the target, return its index
    if arr[mid] == target:
        return mid
    # If the target is less than the middle element, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    # If the target is greater than the middle element, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, right)

def binary_search_iterative(arr, target):
	for x in range(len(arr)):
          if arr[x] == target:
              return x

lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search_recursive(lst, target, 0, len(lst) - 1))
print(binary_search_iterative(lst,target))
