#!/usr/bin/env python3

import math


def g1(x, y):
    return math.sqrt((x * (y + 5) - 1) / 2)


def g2(x, y):
    return math.sqrt(x + 3 * math.log10(x))


i = 0
x = 3.5
y = 2.3
x_old = y_old = False

while x != x_old and y != y_old:
    i += 1
    print("x:", x, "y:", y)
    x_old = x
    y_old = y

    x = g1(x_old, y_old)
    y = g2(x_old, y_old)

print("Final\nx:", x, "y:", y)
print("Iter:", i)
