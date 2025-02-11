# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling demonstration.\n")
    file.write("Writing multiple lines to a file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# Appending to a file
with open("example.txt", "a") as file:
    file.write("Appending a new line to the file.\n")

# Reading file line by line
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())
