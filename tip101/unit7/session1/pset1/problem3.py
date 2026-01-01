def sum_list(lst):
	sum = 0
	while len(lst) > 0:
		sum = sum + lst.pop()
	return sum
inp = [1, 2, 3, 4, 5]
print(sum_list(inp))