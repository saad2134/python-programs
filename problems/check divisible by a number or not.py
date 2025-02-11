def check_divisibility(num, divisor):
    if divisor == 0:
        return "Division by zero is not allowed."
    return f"{num} is divisible by {divisor}." if num % divisor == 0 else f"{num} is not divisible by {divisor}."


num = int(input("Enter a number: "))
divisor = int(input("Enter the divisor: "))


result = check_divisibility(num, divisor)
print(result)
