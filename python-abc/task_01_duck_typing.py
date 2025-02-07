#!/usr/bin/python3
"""
Module task_01_duck_typing
Implémente une classe Shape avec des sous-classes Circle et Rectang
Utilise le duck typing pour afficher l'aire et le pérmètr
"""


from abc import ABC, abstractmethod
import math


print("Import de la classe Shape...")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


print("Import de la classe Circle...")


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


print("Import de la classe Rectangle...")


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


print("Import de la fonction shape_info...")


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
