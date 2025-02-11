def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return sum(int(digit) ** num_digits for digit in num_str) == n

def print_armstrong_numbers(n):
    count, num = 0, 1
    while count < n:
        if is_armstrong(num):
            print(num, end=" ")
            count += 1
        num += 1

n = int(input("Enter how many armstrong numbers: "))
print_armstrong_numbers(n)
