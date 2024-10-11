import pytest

from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_square_int(fixture_example):
    square = Square(3)
    assert square.get_area == 9

@pytest.mark.skip("Decorator 'skip' example")
def test_square_float():
    square = Square(4.5)
    assert square.get_area == 4.5*4.5

@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c", "area"),
    [
        (20, 14, 12, 82.64986388373546),
        (20.1, 14.1, 12.1, 84.02931939954057),
    ],
    ids=["integer", "float"]
)
def test_triangle(side_a, side_b, side_c, area, fixture_just_postcond):
    triangle = Triangle(side_a, side_b, side_c)
    assert triangle.get_area == area

@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [
        (-20, 14, 12),
        (0, 14.1, 12.1),
    ],
    ids=["negative value", "zero value"]
)
def test_triangle_negative(side_a, side_b, side_c, fixture_just_precond):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)

def test_circle():
    circle = Circle(3)
    assert circle.get_area == 28.274333882308138


@pytest.mark.parametrize(
    "radius",
    {
        -20,
        0,
    },
    ids=["negative value", "zero value"]
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)

@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (2, 4, 8),
        (20.0, 4.0, 80.0),
    ],
    ids=["integer", "float"])

def test_rectangle(side_a, side_b, area):
    rectangle = Rectangle(side_a, side_b)
    assert rectangle.get_area == area

@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [
        (-20, 14),
        (0, 14.1),
    ],
    ids=["negative value", "zero value"]
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)