def list_product(lst):
	i = 0
	result = 1
	while i <= len(lst) - 1:
		result = result * lst[i]
		i += 1
	return result
lst = [1, 2, 3, 4, 5]
print(list_product(lst))