def print_even_numbers(n):
    for i in range(2, 2 * n + 1, 2):
        print(i, end=" ")

n = int(input("Enter a number: "))
print_even_numbers(n)
