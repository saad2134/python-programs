def print_multiples(num, n):
    for i in range(1, n + 1):
        print(num * i, end=" ")

num = int(input("Enter a number: "))
n = int(input("Enter how many multiples to print: "))
print_multiples(num, n)
