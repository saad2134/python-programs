# String Initialization
string1 = "Hello"
string2 = "World"

# Concatenation
concatenated = string1 + " " + string2
print("Concatenated String:", concatenated)

# String Repetition
repeated = string1 * 3
print("Repeated String:", repeated)

# String Slicing
sliced = concatenated[0:5]  # Extracts 'Hello'
print("Sliced String:", sliced)

# String Length
length = len(concatenated)
print("Length of Concatenated String:", length)

# String Case Operations
upper_case = string1.upper()
lower_case = string2.lower()
print("Upper Case:", upper_case)
print("Lower Case:", lower_case)

# String Replacement
replaced = concatenated.replace("World", "Python")
print("Replaced String:", replaced)

# String Splitting
split_string = concatenated.split(" ")
print("Split String:", split_string)

# String Stripping
whitespace_str = "  Trim Me  "
trimmed = whitespace_str.strip()
print("Trimmed String:", trimmed)
