#!/usr/bin/python3
"""Module that defines the BaseGeometry class with validation methods."""

class BaseGeometry:
    """Class representing geometry concepts."""

    def area(self):
        """Raises an exception indicating that the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the variable (for error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
