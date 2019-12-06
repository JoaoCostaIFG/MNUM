#!/usr/bin/env python3

import math
from time import sleep

ERRR = 1e-10


def f(x, y):
    return 1 - x**2 - y


def flx(x, y):
    return -2 * x


def fly(x, y):
    return -1


def g(x, y):
    return -y + x + 0.7


def glx(x, y):
    return 1


def gly(x, y):
    return -1


x = y = False
x_new = -1
y_new = 0

while abs(x - x_new) > ERRR or abs(y - y_new) > ERRR:
    x = x_new
    y = y_new
    print("x:", x, "y:", y)

    x_new = x - (f(x, y) * gly(x, y) - g(x, y) * fly(x, y)) / (flx(x, y) * gly(x, y) - glx(x, y) * fly(x, y))
    y_new = y - (g(x, y) * flx(x, y) - f(x, y) * glx(x, y)) / (flx(x, y) * gly(x, y) - glx(x, y) * fly(x, y))


print("Final:\nx:", x, "y:", y)
