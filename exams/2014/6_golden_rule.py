#!/usr/bin/env python3

from math import sin, sqrt


def f(x):
    return x + ((x - 2)**2) / (sin(x) + 4)


B = (sqrt(5) - 1) / 2
A = B**2
x1 = -1
x2 = 1.5
x3 = A * (x2 - x1) + x1
x4 = B * (x2 - x1) + x1

for i in range(2):
    if (f(x3) < f(x4)):
        x2 = x4
        x4 = x3
        x3 = B * (x4 - x1) + x1
    else:
        x1 = x3
        x3 = x4
        x4 = B * (x2 - x3) + x3

    print("iter", i)
    print("x1:", x1, "x2:", x2, "x3:", x3, "x4:", x4)
    print("f(x1)", f(x1), "f(x2)", f(x2), "f(x3)", f(x3), "f(x4)", f(x4))
