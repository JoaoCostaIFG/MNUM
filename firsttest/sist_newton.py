#!/usr/bin/env python3

import math


def f1(x, y):
    return 2 * x**2 - x * y - 5 * x + 1


def f2(x, y):
    return x + 3 * math.log10(x) - y**2


def f1lx(x, y):
    return -y + 4 * x - 5


def f1ly(x, y):
    return -x


def f2lx(x, y):
    return 1 + 3/(math.log(10) * x)


def f2ly(x, y):
    return -2 * y


ERRR = 1e-10
i = 0
x_new = 3.5
y_new = 2.3
x = y = False

while abs(x - x_new) > ERRR and abs(y - y_new) > ERRR:
    i += 1
    print("x:", x, "y:", y)

    x = x_new
    y = y_new

    x_new = x - (f1(x, y) * f2ly(x, y) - f2(x, y) * f1ly(x, y)) / (f1lx(x, y) * f2ly(x, y) - f2lx(x, y) * f1ly(x, y))
    y_new = y - (f2(x, y) * f1lx(x, y) - f1(x, y) * f2lx(x, y)) / (f1lx(x, y) * f2ly(x, y) - f2lx(x, y) * f1ly(x, y))


print("Final\nx:", x_new, "y:", y_new)
print("Iter:", i)
