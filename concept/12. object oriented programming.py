# Encapsulation
class Animal:
    def __init__(self, name):
        self.name = name  # Encapsulation
    
    def speak(self):
        return "Animal sound"

# Inheritance
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism
animals = [Dog("Buddy"), Cat("Whiskers"), Animal("Generic Animal")]

for animal in animals:
    print(f"{animal.name} says: {animal.speak()}")
