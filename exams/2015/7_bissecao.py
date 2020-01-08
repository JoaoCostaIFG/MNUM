#!/usr/bin/env python3

from math import sin


def f(x):
    return x**3 - 10 * sin(x) + 2.8


a = 1.5
b = 4.2
c = 0
for i in range(2):
    c = (b - a) / 2 + a
    if f(c) * f(a) < 0:
        b = c
    else:
        a = c
    print()
