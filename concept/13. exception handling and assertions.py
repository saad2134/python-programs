# Exception Handling
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    print("Execution completed.")

# Using Assertions
def check_positive(number):
    assert number > 0, "Number must be positive"
    print(f"{number} is positive.")

try:
    check_positive(5)
    check_positive(-3)  # This will trigger an assertion error
except AssertionError as ae:
    print("Assertion Error:", ae)
