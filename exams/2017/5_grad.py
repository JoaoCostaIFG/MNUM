#!/usr/bin/env python3


def f(x, y):
    return -1.1 * x * y + 12 * y + 7 * x**2 - 8 * x


def dfdx(x, y):
    return -1.1 * y + 14 * x - 8


def dfdy(x, y):
    return 12 - 1.1 * x


x = 3
y = 1
h = 0.1

nx = x - h * dfdx(x, y)
ny = y - h * dfdy(x, y)
print(nx, ny, f(nx, ny))
