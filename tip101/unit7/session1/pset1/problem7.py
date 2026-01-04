def find_floor(lst, x):
	i = 0
	while i <= len(lst) - 1:
		if x >= lst[i]:
			i += 1
		else:
			return i - 1
	return -1
lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))