def binary_search(lst, target):
	left = 0
	right = len(lst) - 1
	middle = (left + right) // 2
	while left <= right:
		if lst[middle] == target:
			return middle
		elif lst[middle] >= target:
			right = middle
			middle = (left + right) // 2
		elif lst[middle] <= target:
			left = middle
			middle = (left + right) // 2
	return -1
	
lst = [1, 3, 5, 7, 9, 11, 13, 15]
target = 11
print(binary_search(lst, target))