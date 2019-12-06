#!/usr/bin/env python3

import math
from time import sleep


def exprx(x, y):
    return 10 ** ((-x + y**2) / 3)


def expry(x, y):
    return 2 * x - 5 + (1 / x)


def sis_pic(x, y, p):
    x_old = x - 1
    y_old = y - 1

    while (x_old != x) or (y_old != y):
        print("x:", x, "y:", y)
        sleep(0.1)

        x_old = x
        y_old = y

        x = exprx(x_old, y_old)
        y = expry(x_old, y_old)


sis_pic(1, 1, 1e-10)
