#!/usr/bin/env python3

#  In maxima:
#  f: (x - 2.6) + (cos(x + 1.1))^3;
#  diff(f, x);

from math import cos, sin


def f(x):
    return (x - 2.6) + (cos(x + 1.1))**3


def df(x):
    return 1 - 3 * (cos(x + 1.1)**2) * sin(x + 1.1)


x = 1.8
print(x)
x -= f(x) / df(x)
print(x)
