value = input("Enter a positive or negative number: ")

if value > 0:
        print(f"{value} is a positive number.")
elif value < 0:
	print(f"{value} is a negative number.")
else:
	print("The number is zero.")




age = input("Enter an age: ")

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")


