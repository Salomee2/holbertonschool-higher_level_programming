#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            # Transforme la lettre minuscule en majuscule
            char = chr(ord(char) - 32)
        print(char, end="")
    print()
