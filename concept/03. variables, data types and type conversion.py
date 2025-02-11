# Variable Declarations
integer_var = 10  # Integer
float_var = 20.5  # Float
string_var = "Hello, Python!"  # String
boolean_var = True  # Boolean
list_var = [1, 2, 3, 4]  # List
tuple_var = (5, 6, 7)  # Tuple
dict_var = {"name": "Saad", "age": 19}  # Dictionary

# Printing Data Types
print("Data Types Demonstration:")
print("integer_var is of type:", type(integer_var))
print("float_var is of type:", type(float_var))
print("string_var is of type:", type(string_var))
print("boolean_var is of type:", type(boolean_var))
print("list_var is of type:", type(list_var))
print("tuple_var is of type:", type(tuple_var))
print("dict_var is of type:", type(dict_var))

# Type Conversion
converted_int = int(float_var)  # Converting float to int
converted_str = str(integer_var)  # Converting int to string
converted_list = list(tuple_var)  # Converting tuple to list

print("\nType Conversion Demonstration:")
print("Converted float_var to int:", converted_int)
print("Converted integer_var to string:", converted_str)
print("Converted tuple_var to list:", converted_list)
