#!/usr/bin/env python3

a = 1.2
b = 1.0


def f(x, y):
    return x**2 - y - a


def fx(x, y):
    return 2 * x


def fy(x, y):
    return -1


def g(x, y):
    return -x + y**2 - b


def gx(x, y):
    return -1


def gy(x, y):
    return 2 * y


x = 1
y = 1
for i in range(2):
    denom = fx(x, y) * gy(x, y) - gx(x, y) * fy(x, y)
    nx = x - (f(x, y) * gy(x, y) - g(x, y) * fy(x, y)) / denom
    ny = y - (g(x, y) * fx(x, y) - f(x, y) * gx(x, y)) / denom

    x = nx
    y = ny
    print("x:", x, "y:", y)
