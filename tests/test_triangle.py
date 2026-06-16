from src.circle import Circle
from src.rectangle import Rectangle
import pytest
from src.square import Square
from src.triangle import Triangle

@pytest.mark.usefixtures("preparation_before_class")
class TestTriangleForOneRun:
    
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("type_of_number",
                             ["int", "float", "int and float"],
                             ids=["int", "float", "int and float"])
    def test_triangle_area_positive(self, test_fixture_for_triangle_area: tuple[int|float, int|float, int|float, int|float,],\
                                    type_of_number: str) -> None:
        side_a, side_b, side_c, expected = test_fixture_for_triangle_area(type_of_number=type_of_number)
        assert round(Triangle(side_a, side_b, side_c).area, 2) == expected, (
            f"Incorrect value for area of triangle with sides {side_a}, {side_b}, {side_c}: "
            f"expected {expected}, actual {round(Triangle(side_a, side_b, side_c).area, 2)}")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.parametrize("type_of_number",
        ["int", "float", "int and float"],
        ids=["int", "float", "int and float"],)
    def test_triangle_perimetr_positive(self, test_fixture_for_triangle_perimetr: tuple[int|float, int|float, int|float, int|float],
                                        type_of_number: str) -> None:
        side_a, side_b, side_c, expected = test_fixture_for_triangle_perimetr(type_of_number=type_of_number)
        assert round(Triangle(side_a, side_b, side_c).perimetr, 2) == expected, (
            f"Incorrect value for perimetr of square with sides {side_a}, {side_b}, {side_c}: "
            f"expected {expected}, actual {round(Triangle(side_a, side_b, side_c).perimetr, 2)}")

    @pytest.mark.negative
    @pytest.mark.parametrize("side_a, side_b, side_c",
        [pytest.param(3, 0, 8, id="zero value"),
         pytest.param(6, 7.3, -1, id="negative value"),
         pytest.param(4, 4, 8, id="side equal sum others"),
         pytest.param(4, 5, 10, id="one side more than sum others")])
    def test_triangle_negative(self, side_a: int|float, side_b: int|float, side_c: int|float) -> None:
        with pytest.raises(ValueError, match=f"Triangle with sides {side_a}, {side_b}, {side_c} cannot exist"):
            Triangle(side_a, side_b, side_c)

    @pytest.mark.regression
    @pytest.mark.parametrize("other_figure, expected",
        [pytest.param(Rectangle(2, 3), 7.84, id="rectangle"),
         pytest.param(Square(4), 17.84, id="square"),
         pytest.param(Circle(3.3), 36.05, id="circle"),
        pytest.param(Triangle(4, 4, 4), 8.77, id="triangle")])
    def test_triangle_add_area_with_different_figure(self, other_figure: Rectangle|Square|Circle|Triangle,
                                                      expected: int | float,) -> None:
        assert round(Triangle(2, 2, 2.2).add_area(other_figure), 2) == expected, (
            f"Incorrect sum of areas: expected {expected}, actual {round(Triangle(2, 2, 2.2).add_area(other_figure), 2)}")

    @pytest.mark.negative
    def test_triangle_add_area_with_number_negative(self, number: int|float = 5.5) -> None:
        with pytest.raises(ValueError, match="Should be a Figure"):
            Triangle(3, 3,3).add_area(number)
