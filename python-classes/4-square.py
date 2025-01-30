#!/usr/bin/python3
""" module containing def of a square class"""


class Square:
    """Représente un carré."""

    def __init__(self, size=0):
        """Initialize a square with a private size"""
        self.size = size

    @property
    def size(self):
        """to get the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """to change size with checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
