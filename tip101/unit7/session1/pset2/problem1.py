def countdown(n):
	if n > 0:
		print(n)
		countdown(n - 1)
		
countdown(5)

def countdown_iterative(n):
	for x in range(n):
		print(n-x)
countdown_iterative(5)