def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}.")


def add_numbers(n1,n2):
	return n1+n2
print(add_numbers(2, 5))
