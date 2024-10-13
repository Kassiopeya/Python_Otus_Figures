from abc import ABC, abstractmethod
from src.figure import Figure
import math


class Circle (Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius can't be less than 0")
        self.radius = radius

    @property
    def get_area(self):
        area = math.pi*self.radius**2
        return round (area, 2)

    @property
    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)
