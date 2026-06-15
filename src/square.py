from rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side_a: int|float) -> None:
        if side_a <= 0:
            raise ValueError("Sides can't be less than 0")
        super().__init__(side_a, side_a)
