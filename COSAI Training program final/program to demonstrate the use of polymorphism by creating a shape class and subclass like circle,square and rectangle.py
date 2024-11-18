import math

class Shape:
    def area(self):
        """Base method for calculating area, meant to be overridden."""
        raise NotImplementedError("Subclasses must implement the area method.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """Calculate the area of a square."""
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of a rectangle."""
        return self.width * self.height

def print_area(shape):
    """A polymorphic function to print the area of any shape."""
    print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)

    for shape in [circle, square, rectangle]:
        print_area(shape)
