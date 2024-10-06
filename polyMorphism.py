# Base class: Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    # Overriding the area method
    def area(self):
        return 3.14 * self.radius ** 2

    # Overriding the perimeter method
    def perimeter(self):
        return 2 * 3.14 * self.radius

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Overriding the area method
    def area(self):
        return self.length * self.width

    # Overriding the perimeter method
    def perimeter(self):
        return 2 * (self.length + self.width)

# Derived class: Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Overriding the perimeter method
    def perimeter(self):
        return self.a + self.b + self.c

    # Method overloading-like behavior with default arguments for area
    def area(self, height=None):
        if height is not None:
            # Assuming this is an equilateral triangle with a given height
            return 0.5 * self.b * height
        else:
            # Return a message if height is not provided
            return "Can't calculate area without height for a triangle!"

# Function demonstrating polymorphism
def display_shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Main program to test polymorphism
if __name__ == "__main__":
    # Creating objects of derived classes
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5)

    # Using polymorphism to call the area and perimeter methods
    print("Circle Info:")
    display_shape_info(circle)

    print("\nRectangle Info:")
    display_shape_info(rectangle)

    print("\nTriangle Info (without height for area):")
    display_shape_info(triangle)

    print("\nTriangle Info (with height for area):")
    # Calling the area method with height to simulate method overloading
    print(f"Area with height: {triangle.area(height=6)}")
    print(f"Perimeter: {triangle.perimeter()}")
