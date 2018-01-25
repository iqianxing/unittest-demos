import pytest


def func(x, y):
    return x + y


def test_answer():
    assert func(3, 2) == 5
