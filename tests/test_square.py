import pytest
from src.square import Square


def test_square_int(fixture_example):
    square = Square(3)
    assert square.get_area == 9

@pytest.mark.skip("Decorator 'skip' example")
def test_square_float():
    square = Square(4.5)
    assert square.get_area == 4.5*4.5