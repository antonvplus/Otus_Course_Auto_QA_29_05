from src.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, side_a: int|float) -> None:
        if side_a <= 0:
            raise ValueError("Side cannot be less than or equal to 0")
        super().__init__(side_a, side_a)
