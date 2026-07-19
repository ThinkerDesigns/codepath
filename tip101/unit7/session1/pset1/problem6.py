# WIP
def find_last(lst, target):
	left = 0
	right = len(lst) - 1
	middle = (left + right) // 2
	lastIdx = 0
	while left <= right:
		if lst[middle] == target:
			lastIdx = middle
			left = middle
			middle = (left + right) // 2
		elif lst[middle] >= target:
			right = middle
			middle = (left + right) // 2
		elif lst[middle] <= target:
			left = middle
			middle = (left + right) // 2
	return lastIdx
lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
target = 11
print(find_last(lst,target))