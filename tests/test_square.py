from src.circle import Circle
from src.rectangle import Rectangle
import pytest
from src.square import Square
from src.triangle import Triangle


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("side, expected",
    [pytest.param(3, 9, id="int"),
    pytest.param(3.6, 12.96, id="float")])
def test_square_area_positive(preparation_before_test: None, side: int | float, expected: int | float,) -> None:
    assert Square(side).area == expected, (
        f"Incorrect value for area of square with side {side}: expected {expected}, actual {Square(side).area}")

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("side, expected",
    [pytest.param(2, 8, id="int"),
     pytest.param(5.5,22.0, id="float")])
def test_square_perimetr_positive(preparation_before_test: None, side: int | float, expected: int | float) -> None:
    assert Square(side).perimetr == expected, (
        f"Incorrect value for perimetr of square with side {side}: expected {expected}, actual {Square(side).perimetr}")


@pytest.mark.negative
@pytest.mark.parametrize("side",
    [pytest.param(0, id="zero value"), pytest.param(-3, id="negative value")])
def test_square_negative(preparation_before_test: None, side: int | float) -> None:
    with pytest.raises(ValueError, match="Side cannot be less than or equal to 0"):
        Square(side)

@pytest.mark.regression
@pytest.mark.parametrize("other_figure, expected",
    [
        pytest.param(Rectangle(6, 7), 46, id="rectangle"),
        pytest.param(Square(4.2), 21.64, id="square"),
        pytest.param(Circle(6), 117.1, id="circle"),
        pytest.param(Triangle(4, 5, 6), 13.92, id="triangle"),
    ])
def test_square_add_area_with_different_figure(preparation_before_test: None,
                                                other_figure: Rectangle | Square | Circle | Triangle, expected: int | float) -> None:
    assert round(Square(2).add_area(other_figure), 2) == expected, (
        f"Incorrect sum of areas: expected {expected}, actual {round(Square(2).add_area(other_figure), 2)}"
    )


@pytest.mark.negative
def test_square_add_area_with_number_negative(preparation_before_test: None, number: int | float = 3.3) -> None:
    with pytest.raises(ValueError, match="Should be a Figure"):
        Square(3).add_area(number)
