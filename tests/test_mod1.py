import numpy as np
import pytest

from mymodule.mod1 import NormalMyAdder, ListMyAdder, NumpyMyAdder


@pytest.mark.parametrize('a, b, answer', [
    (0, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, -2, -1),
    (-2, 1, -1),
])
def test_normal_my_adder(a, b, answer):
    adder = NormalMyAdder(a, b)
    assert adder.add() == answer


@pytest.mark.parametrize('a, b, answer', [
    (0, 0, [0]),
    (1, 0, [1]),
    (0, 1, [1]),
    (1, -2, [-1]),
    (-2, 1, [-1]),
])
def test_list_my_adder(a, b, answer):
    adder = ListMyAdder(a, b)
    assert adder.add() == answer


@pytest.mark.parametrize('a, b, answer', [
    (0, 0, np.array([0])),
    (1, 0, np.array([1])),
    (0, 1, np.array([1])),
    (1, -2, np.array([-1])),
    (-2, 1, np.array([-1]))
])
def test_numpy_my_adder(a, b, answer):
    adder = NumpyMyAdder(a, b)
    assert adder.add() == answer
