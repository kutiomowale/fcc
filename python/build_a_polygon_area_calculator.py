#!/usr/bin/env python3
from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        result = "*" * self.width + '\n'
        result *= self.height
        return result

    def get_amount_inside(self, shape):
        """
        Returns the number of times the passed in shape could fit inside
        the shape (with no rotations). For instance, a rectangle with a
        width of 4 and a height of 8 could fit in two squares with sides of 4
        """
        if shape.height > self.height or shape.width > self.width:
            return 0
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_side(self, side):
        self.width = side
        self.height = side


def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))


if __name__ == '__main__':
    main()
