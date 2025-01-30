#!/usr/bin/python3
""" Module containing def of a square class"""


class Square:
    """Représente un carré."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a private size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter to modify size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter to get the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter to change position with checking"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of square"""
        return self.__size ** 2

    def my_print(self):
        """Displays the square in # while respecting position"""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
