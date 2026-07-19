# WIP
def ternary_search(lst, target):
	left = 0
	right = len(lst) - 1
	mid1 = (left + right) // 3
	mid2 = (mid1 + right) // 2
	middle = (left + right) // 3
	while left <= right:
		if target == lst[mid1]:
			return mid1
		elif target == lst[mid2]:
			return mid2
		elif target <= lst[mid1]:
			right = mid1 - 1
			mid1 = (left + right) // 3
		elif lst[mid1] <= target <= lst[mid2]:
			left = mid1 + 1
			right = mid2 - 1
			middle = (left + right) // 3
		elif target >= lst[mid2]:
			left = mid2 + 1
			middle = (left + right) // 3
			
			
	return -1
  # Divide the array into three parts using two mid points (mid1 and mid2).
  
  # While the lower bound is less than or equal to the upper bound:
	  # Compare the target value with the values at mid1 and mid2:
	      # If the target value matches mid1 or mid2
		      # the search is successful.
	      # If the target is less than the value at mid1
		      # search between the lower bound and mid1 - 1.
	      # If the target is between mid1 and mid2
		      # search between mid1 + 1 and mid2 - 1.
	      # If the target is greater than the value at mid2
		      # search between mid2 + 1 and the upper bound.
  # Return -1, indicating the target is not in the array.
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(ternary_search(lst,target))