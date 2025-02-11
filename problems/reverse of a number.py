def reverse_number(n):
    reversed_num = int(str(abs(n))[::-1])  
    if n < 0:
        reversed_num *= -1  
    return reversed_num

num = int(input("Enter a number: "))
print(f"Reversed Number: {reverse_number(num)}")