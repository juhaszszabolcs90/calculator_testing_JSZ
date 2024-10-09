import pytest
from calculator import sum, substraction, multiply, division

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, 2) == 1
    assert sum(-1, -2) == -3
    assert sum(0, 0) == 0

def test_substraction():
    assert substraction(5, 2) == 3
    assert substraction(-1, 2) == -3
    assert substraction(-1, -2) == 1
    assert substraction(0, 0) == 0