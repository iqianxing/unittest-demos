import pytest


def caculater(x, y):
    return x + y

def test_caculater():
    assert caculater(3, 2) == 5
