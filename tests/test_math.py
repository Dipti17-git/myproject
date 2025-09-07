
from src.calculator import add
def test_addition():
    assert 2 + 2 == 4


def test_add():
    assert add(3, 4) == 7
