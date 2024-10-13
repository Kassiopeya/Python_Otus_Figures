import pytest

from src.triangle import Triangle


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