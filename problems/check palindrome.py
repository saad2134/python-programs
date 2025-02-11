def is_palindrome(n):
    return str(n) == str(n)[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
