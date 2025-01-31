#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by width and height,
with methods for calculating the area
perimeter, and handling instance deletion.
"""


class Rectangle:
    """Represent a rectangle by its width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the number of instances

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the string representation of
        the rectangle using print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = [
            str(self.__width * "#") for _ in range(self.__height)
        ]
        return "\n".join(rectangle_str)

    def __repr__(self):
        """Return a string that can recreate the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
