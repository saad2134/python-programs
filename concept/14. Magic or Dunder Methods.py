
# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__, etc

# They are automatically called by many of Python's built-in operations. They allow developers to define or customize the behavior of objects


class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name} & GPA: {self.gpa}"

    def __eq__ (self, other):
        return self.name == other.name

    def __lt__ (self, other):
        return self.gpa < other.gpa

    def __gt__ (self, other):
        return self.gpa > other.gpa

std1 = Student ("Alex", 8.99)
std2 = Student("John", 7.86)

print(std1)
print(std2)

print(std1 == std2)
print(std1 < std2)
print(std1 > std2)
