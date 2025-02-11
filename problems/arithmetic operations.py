def calculate_operations(a, b):
    print(f"Sum: {a} + {b} = {a + b}")
    print(f"Difference: {a} - {b} = {a - b}")
    print(f"Product: {a} * {b} = {a * b}")
    
    if b != 0:
        print(f"Quotient: {a} / {b} = {a / b}")
        print(f"Remainder: {a} % {b} = {a % b}")
    else:
        print("Division and modulus by zero are not allowed.")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

calculate_operations(a, b)
