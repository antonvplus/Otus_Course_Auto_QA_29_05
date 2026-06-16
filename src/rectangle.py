from src.figure import Figure

class Rectangle(Figure):

    def __init__(self, side_a: int|float, side_b: int|float) -> None:
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Sides cannot be less than or equal to 0")
        self.side_a = side_b
        self.side_b = side_a

    @property
    def area(self) -> int|float:
        return self.side_a * self.side_b

    @property
    def perimetr(self) -> int|float:
        return (self.side_a + self.side_b) * 2
