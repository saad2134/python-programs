def print_odd_numbers(n):
    for i in range(1, 2 * n, 2):
        print(i, end=" ")

n = int(input("Enter a number: "))
print_odd_numbers(n)
