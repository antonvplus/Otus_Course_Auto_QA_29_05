from src.circle import Circle
from src.rectangle import Rectangle
import pytest
from src.square import Square
from src.triangle import Triangle

@pytest.mark.usefixtures("preparation_before_class")
class TestCircleForOneRun:
    
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(("radius", "expected"),
        [(2, 12.57), (3.3, 34.21)],
        ids=["int", "float"])
    def test_circle_area_positive(self, radius: int | float, expected: int | float) -> None:
        assert round(Circle(radius).area, 2) == expected, (
            f"Incorrect value for area of circle with radius {radius}: expected {expected}, actual {round(Circle(radius).area, 2)}")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize(("radius", "expected"),
                             [(4, 25.13), (3.3, 20.73)],
                             ids=["int", "float"])
    def test_circle_perimetr_positive(self, radius: int | float, expected: int | float) -> None:
        assert round(Circle(radius).perimetr, 2) == expected, (
            f"Incorrect value for area of circle with radius {radius}: expected {expected}, actual {round(Circle(radius).perimetr, 2)}")

    @pytest.mark.negative
    @pytest.mark.parametrize("radius",
        [0, -3],
        ids=["zero value", "negative value"])
    def test_circle_negative(self, radius: int | float) -> None:
        with pytest.raises(ValueError, match="Radius can't be less than or equal to 0"):
            Circle(radius)

    @pytest.mark.regression
    @pytest.mark.parametrize(("other_figure", "expected"),
        [(Rectangle(3, 5), 168.94),
         (Square(4), 169.94),
         (Circle(5), 232.48),
         (Triangle(2, 3, 4), 156.84)],
         ids=["rectangle", "square", "circle", "triangle"])
    def test_circle_add_area_with_different_figure(self, other_figure: Rectangle|Square|Circle|Triangle, expected: int|float) -> None:
        assert round(Circle(7).add_area(other_figure), 2) == expected, (
            f"Incorrect sum of areas: expected {expected}, actual {round(Circle(7).add_area(other_figure), 2)}")

    @pytest.mark.negative
    def test_circle_add_area_with_number_negative(self, number: int|float = 2) -> None:
        with pytest.raises(ValueError, match="Should be a Figure"):
            Circle(4).add_area(number)
