#!/usr/bin/python3
"""
This module contains a function that prints a text with two new lines
after each of the characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints the given text with two new lines after each of the characters:
    '.', '?', and ':'.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through the text and print the text with indentation
    temp = ""
    for char in text:
        temp += char
        if char in ['.', '?', ':']:
            print(temp.strip())
            print()
            temp = ""
    if temp:
        print(temp.strip())
