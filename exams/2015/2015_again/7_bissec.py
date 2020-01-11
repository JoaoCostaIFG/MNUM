#!/usr/bin/env python3

from math import sin


def f(x):
    return x**3 - 10 * sin(x) + 2.8


a = 1.5
b = 4.2
print(a, b)

for i in range(2):
    c = (b - a) / 2 + a
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    print(a, b)
