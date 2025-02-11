# Demonstrating Function Recursion in Python

def factorial(n):
    """Recursively calculates the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the recursive function
num = 5
print(f"Factorial of {num} is {factorial(num)}")


def fibonacci(n):
    """Recursively calculates the nth Fibonacci number."""
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Testing the Fibonacci function
fib_num = 6
print(f"{fib_num}th Fibonacci number is {fibonacci(fib_num)}")
