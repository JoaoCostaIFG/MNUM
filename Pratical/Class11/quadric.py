#!/usr/bin/env python3

from math import sqrt


def dist(x, x2):
    return sqrt((x2[0] - x[0])**2 + (x2[1] - x[1])**2 + (x2[2] - x[2])**2)


def f(x, y):
    # function
    return (y - x**2)**2


def grad(x, y, z):
    # gradient of f
    return [4*x**3 - 4*x*y, 2*y - 2*x**2, 0]


# init conds
x = [99991, 9992, f(99991, 9992)]
lamb = 1000

while abs(lamb) > 0.001:
    gr = grad(*x)
    newx = [x[0] - lamb * gr[0], x[1] - lamb * gr[1]]
    newx[2] = f(newx[0], newx[1])

    if (f(*x[:-1]) > f(*newx[:-1])):
        lamb *= 2

print("result:", x)
