principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time (in years): "))

amount = principal * (1 + rate / 100) ** time
ci = amount - principal

print(f"Compound Interest: {ci:.2f}")
print(f"Total Amount: {amount:.2f}")
