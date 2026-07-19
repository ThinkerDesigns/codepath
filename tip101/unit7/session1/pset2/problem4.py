def is_power_of_four(n):
	if n == 4:
		return True
	elif n % 4 != 0:
		return False
	else:
		return is_power_of_four(n//4)

n = 16
print(is_power_of_four(n))
n = 8
print(is_power_of_four(n))