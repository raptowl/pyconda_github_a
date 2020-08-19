import numpy as np


class MyAdder():
    def __init__(self, num_a: int, num_b: int):
        self.num_a = num_a
        self.num_b = num_b

    def add(self):
        raise NotImplementedError()


class NormalMyAdder(MyAdder):
    def add(self):
        c = self.num_a + self.num_b
        return c


class ListMyAdder(MyAdder):
    def add(self):
        num_c = self.num_a + self.num_b
        c = [num_c]
        return c


class NumpyMyAdder(MyAdder):
    def add(self):
        num_c = self.num_a + self.num_b
        c = np.array([num_c])
        return c
