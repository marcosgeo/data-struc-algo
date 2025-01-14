import pytest
from . import factorial, fibonacci


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (0, 1),
    (1, 1),
    (-1, 1),
    (-10, 1)
])
def test_factorial(n, expected):
    assert factorial(n) == expected


@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55)
])
def test_fibonnaci(n, expected):
    result = fibonacci(n)
    assert result == expected
