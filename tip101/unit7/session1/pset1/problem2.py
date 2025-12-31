def factorial(n):
	if n == (1 or 0):
		return 1
	elif n == 2:
		return 2
	else:
		return (n) * factorial(n-1)
inp = 5
print(factorial(5))