# Base class
class Animal:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age

    def sound(self):  # Method that will be overridden
        return "Some generic animal sound"

    def info(self):  # Method to display information
        print(f"{self.name} is {self.age} years old.")

# Derived class 1: Dog inherits from Animal
class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call the base class constructor using super()
        super().__init__(name, age)
        self.breed = breed  # Additional attribute specific to Dog

    # Overriding the base class sound method
    def sound(self):
        return "Woof! Woof!"

    # Additional method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Derived class 2: Cat inherits from Animal
class Cat(Animal):
    def __init__(self, name, age, color):
        # Call the base class constructor
        super().__init__(name, age)
        self.color = color  # Additional attribute specific to Cat

    # Overriding the base class sound method
    def sound(self):
        return "Meow! Meow!"

    # Additional method specific to Cat
    def climb(self):
        print(f"{self.name} is climbing a tree.")

# Demonstrating inheritance and method overriding
if __name__ == "__main__":
    # Creating a Dog object
    dog = Dog("Buddy", 3, "Golden Retriever")
    print("Dog Info:")
    dog.info()  # Accessing the base class method
    print(f"Breed: {dog.breed}")
    print(f"Sound: {dog.sound()}")  # Accessing overridden method
    dog.fetch()  # Accessing derived class method
    
    # Creating a Cat object
    cat = Cat("Whiskers", 2, "Black")
    print("\nCat Info:")
    cat.info()  # Accessing the base class method
    print(f"Color: {cat.color}")
    print(f"Sound: {cat.sound()}")  # Accessing overridden method
    cat.climb()  # Accessing derived class method
