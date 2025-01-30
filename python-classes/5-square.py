#!/usr/bin/python3
""" module containing def of square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize a square with a private size"""
        self.size = size

    @property
    def size(self):
        """Getter to get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to change size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """displays the square in # """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
