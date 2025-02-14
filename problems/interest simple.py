principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time (in years): "))

si = (principal * rate * time) / 100
amount = principal + si

print(f"Simple Interest: {si:.2f}")
print(f"Total Amount: {amount:.2f}")
