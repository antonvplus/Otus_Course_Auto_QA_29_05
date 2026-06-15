from figure import Figure
from math import sqrt

class Triangle(Figure):

    def __init__(self, side_a: int|float, side_b: int|float, side_c: int|float) -> None:
        if (any(side <= 0 for side in [side_a, side_b, side_c])
                or sum(sorted([side_a, side_b, side_c])[0:2]) <= max([side_a, side_b, side_c])):
            raise ValueError(f"Triangle with sides {side_a}, {side_b}, {side_c} cannot exist")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self) -> int|float:
        semiperimeter = (self.side_a + self.side_b + self.side_c) / 2
        return sqrt(semiperimeter * (semiperimeter - self.side_a) * (semiperimeter - self.side_b) * (semiperimeter - self.side_c))

    @property
    def perimetr(self) -> int|float:
        return self.side_a + self.side_b + self.side_c
