class Rectangle:
    def __init__(self, length, width):
        self.set_dimensions(length, width)

    def set_dimensions(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"

    def compare_area(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError("Can only compare area with another Rectangle.")
        if self.area() > other.area():
            return f"{self} has a larger area than {other}."
        elif self.area() < other.area():
            return f"{self} has a smaller area than {other}."
        else:
            return f"{self} and {other} have the same area."

class Square(Rectangle):
    def __init__(self, side_length):
        self.set_dimensions(side_length, side_length)

    def __str__(self):
        return f"Square(side_length={self.length})"

# Testing the classes
if __name__ == "__main__":
    try:
        rect1 = Rectangle(5, 3)
        rect2 = Rectangle(2, 7)
        square = Square(4)

        print(rect1)                 # Output: Rectangle(length=5, width=3)
        print(f"Area of rect1: {rect1.area()}")  # Output: Area of rect1: 15
        print(square)               # Output: Square(side_length=4)
        print(f"Area of square: {square.area()}")  # Output: Area of square: 16

        print(rect1.compare_area(rect2))  # Output: Rectangle(length=5, width=3) has a larger area than Rectangle(length=2, width=7).
        print(rect1.compare_area(square))  # Output: Rectangle(length=5, width=3) has a smaller area than Square(side_length=4).

    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
