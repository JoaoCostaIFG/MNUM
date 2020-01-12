#!/usr/bin/env python3

import math
from time import sleep

ERRR = 1e-10


def f(x, y):
    return -math.sqrt(1 - y)


def g(x, y):
    return 0.7 + x


def f2(x, y):
    return y - 0.7


def g2(x, y):
    return 1 - x**2


x = y = False
x_new = 0
y_new = 0.5

while abs(x - x_new) > ERRR or abs(y - y_new) > ERRR:
    x = x_new
    y = y_new
    print("x:", x, "y:", y)

    x_new = f(x, y)
    y_new = g(x, y)

print("Final:\nx:", x, "y:", y)
