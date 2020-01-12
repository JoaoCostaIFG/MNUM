#!/usr/bin/env python3

from math import cos, sin, sqrt


def f(x):
    return 5 * cos(x) - sin(x)


B = (sqrt(5) - 1) / 2
A = B**2

x1 = 2
x2 = 4
x3 = x1 + A * (x2 - x1)
x4 = x1 + B * (x2 - x1)
print(x1, x2, x3, x4)
print(f(x1), f(x2), f(x3), f(x4), "\n")

for i in range(2):
    if f(x3) < f(x4):
        x2 = x4
        x4 = x3
        x3 = x1 + A * (x2 - x1)
    else:
        x1 = x3
        x3 = x4
        x4 = x1 + B * (x2 - x1)
    print(x1, x2, x3, x4)
    print(f(x1), f(x2), f(x3), f(x4), "\n")

print(x2 - x1)
