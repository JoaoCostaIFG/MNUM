#!/usr/bin/env python3

import math


def f(x):
    return ((math.cos(x + 1.2)) ** 3) - 3.6 + x


def fl(x):
    x += 1.2
    return 1 - 3 * ((math.cos(x))**2) * math.sin(x)


x = 0.5

x = x - (f(x) / fl(x))

print(x)

