# This is a Python program to calculate the factorial of a number

def factorial(n):
    """This function calculates the factorial of a given number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Input
num = 5

# Calculate the factorial
result = factorial(num)

# Output
print(f"The factorial of {num} is {result}")
