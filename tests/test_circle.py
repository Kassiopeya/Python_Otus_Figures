import pytest

from src.circle import Circle


def test_circle():
    circle = Circle(3)
    assert circle.get_area == 28.27


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