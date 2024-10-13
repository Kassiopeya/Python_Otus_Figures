import pytest

from src.circle import Circle
from src.square import Square
from src.triangle import Triangle


def test_add_circle_to_square():
    circle = Circle(3)
    square = Square(2)
    assert round(circle.add_area(square), 2) == 32.27
    # Почему здесь приходится снова округлять площадь круга?
    # Если здесь не поставить round - тест валится из-за того, что circle.get_area возвращает неокруглённое число

def test_add_triangle_to_square():
    triangle = Triangle(20.1,14.1,12.1)
    square = Square(6)
    assert  triangle.add_area(square) == 84.03 + 36

def test_negative_test():
    triangle = Triangle(20.1, 14.1, 12.1)
    invalid_figure = 4.0

    with pytest.raises(ValueError):
       triangle.add_area(invalid_figure)