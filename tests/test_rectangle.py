from src.circle import Circle
from src.rectangle import Rectangle
import pytest
from src.square import Square
from src.triangle import Triangle

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("side_a, side_b, expected", [
    pytest.param(4, 5, 20, id="int"),
    pytest.param(6.5, 7.4, 48.1, id="float"),
    pytest.param(4, 3.5, 14.0, id="int and float")])
def test_rectangle_area_positive(preparation_before_test: None, side_a: int|float, side_b: int|float, expected: int|float) -> None:
    assert Rectangle(side_a, side_b).area == expected, \
        (f"Incorrect value for area of rectangle with sides {side_a} and {side_b}: expected {expected}, "
         f"actual {Rectangle(side_a, side_b).area}")

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("side_a, side_b, expected", [
    pytest.param(2, 3, 10, id="int"),
    pytest.param(4.7, 5.5, 20.4, id="float"),
    pytest.param(3, 3.2, 12.4, id="int and float")])
def test_rectangle_perimetr_positive(preparation_before_test: None, side_a: int|float, side_b: int|float, expected: int|float) -> None:
    assert Rectangle(side_a, side_b).perimetr == expected, \
        (f"Incorrect value for perimetr of rectangle with sides {side_a} and {side_b}: expected {expected}, "
         f"actual {Rectangle(side_a, side_b).perimetr}")

@pytest.mark.negative
@pytest.mark.parametrize("side_a, side_b", [
    pytest.param(4, 0, id="zero value"),
    pytest.param(-6.5, 7.4, id="negative value")])
def test_rectangle_negative(preparation_before_test: None, side_a: int|float, side_b: int|float) -> None:
    with pytest.raises(ValueError, match='Sides cannot be less than or equal to 0'):
        Rectangle(side_a, side_b)

@pytest.mark.regression
@pytest.mark.parametrize("other_figure, expected", [
    pytest.param(Rectangle(6, 7), 57, id="rectangle"),
    pytest.param(Square(4.2), 32.64, id="square"),
    pytest.param(Circle(6), 128.1, id="circle"),
    pytest.param(Triangle(4, 5, 6), 24.92, id="triangle")])
def test_rectangle_add_area_with_different_figure(preparation_before_test: None,
                                                  other_figure: Rectangle|Square|Circle|Triangle, expected: int|float) -> None:
    assert round(Rectangle(3, 5).add_area(other_figure), 2) == expected, \
        f"Incorrect sum of areas: expected {expected}, actual {round(Rectangle(3, 5).add_area(other_figure), 2)}"

@pytest.mark.negative
def test_rectangle_add_area_with_number_negative(preparation_before_test: None,
                                                  number: int|float=5) -> None:
    with pytest.raises(ValueError, match="Should be a Figure"):
        Rectangle(3, 5).add_area(number)
