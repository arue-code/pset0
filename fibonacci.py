#!/usr/bin/env python3

import numpy as np


def last_8(some_int):
    """Return the last 8 digits of an int

    :param int some_int: the number
    :rtype: int
    """

    lasteight = some_int % 100000000
    return lasteight


def optimized_fibonacci(f):
    fibm = np.matrix([[1, 1], [1, 0]])
    initial = np.array([1, 1])
    finalmatrix = np.linalg.matrix_power(fibm, f - 1)
    fibnum = np.matmul(finalmatrix, initial)
    return fibnum[0, 1]


class SummableSequence(object):
    def __init__(self, *args, **kwargs):
        # self.__dict__.update(**kwargs)
        self.myAttr = args

    def __call__(self, i, *args, **kwargs):
        # fibm = np.matrix([1])
        fibm = np.matrix([[0, 1, 0], [0, 0, 1], [1, 1, 1]], dtype=object)
        initial = np.array(self.myAttr, dtype=object)
        finalmatrix = np.linalg.matrix_power(fibm, i)
        fibnum = np.matmul(finalmatrix, initial)
        return fibnum[0, 0]


if __name__ == "__main__":

    print("f(100000)[-8:]", last_8(optimized_fibonacci(100000)))

    ss = SummableSequence(0, 1)
    new_seq = SummableSequence(5, 7, 11)
    print("new_seq(100000)[-8:]:", last_8(new_seq(100000)))

    print("new_seq(0)[-8:]", last_8(new_seq(0)))
    print("new_seq(1)[-8:]", last_8(new_seq(1)))
    print("new_seq(2)[-8:]", last_8(new_seq(2)))
    print("new_seq(3)[-8:]", last_8(new_seq(3)))
    print("new_seq(4)[-8:]", last_8(new_seq(4)))
    print("new_seq(5)[-8:]", last_8(new_seq(5)))
    print("new_seq(6)[-8:]", last_8(new_seq(6)))
