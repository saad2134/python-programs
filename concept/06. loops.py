# For Loop
print("For Loop Example:")
for i in range(5):
    print("Iteration", i)

# While Loop
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print("Iteration", count)
    count += 1

# Nested Loop
print("\nNested Loop Example:")
for i in range(3):
    for j in range(2):
        print(f"Outer loop {i}, Inner loop {j}")

# Loop with Break
print("\nLoop with Break:")
for i in range(5):
    if i == 3:
        print("Breaking at", i)
        break
    print("Iteration", i)

# Loop with Continue
print("\nLoop with Continue:")
for i in range(5):
    if i == 2:
        print("Skipping", i)
        continue
    print("Iteration", i)

# Loop with Else
print("\nLoop with Else:")
for i in range(3):
    print("Iteration", i)
else:
    print("Loop completed without break.")
