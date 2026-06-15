from figure import Figure
from math import pi

class Circle(Figure):

    def __init__(self, radius: int|float) -> None:
        if radius <= 0:
            raise ValueError("Radius can't be less than 0")
        self.radius = radius

    @property
    def area(self) -> int|float:
        return pi * self.radius**2

    @property
    def perimetr(self) -> int|float:
        return 2 * pi * self.radius



