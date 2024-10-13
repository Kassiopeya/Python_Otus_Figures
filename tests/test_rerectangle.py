import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize(
    ("side_a", "side_b", "area"),
    [
        (2, 4, 8),
        (20.0, 4.0, 80.0),
    ],
    ids=["integer", "float"])

def test_rectangle_area(side_a, side_b, area):
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