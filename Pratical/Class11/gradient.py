#!/usr/bin/env python3

from math import sqrt


def dist(x, x2):
    return sqrt((x2[0] - x[0])**2 + (x2[1] - x[1])**2 + (x2[2] - x[2])**2)


def f(x, y):
    # function
    return x**2 + y**2


def grad(x, y, z):
    # gradient of f
    return [2*x, 2*y, 0]


# init conds
x = [15, 15, f(15, 15)]
lamb = 2

xold = [99, 99, f(99, 99)]
while dist(xold, x) > 0.5 and lamb >= 0.0001:
    print("x:", x)
    print("xold", xold)
    xnew = grad(*x)
    xnew = [x[0] - lamb * xnew[0], x[1] - lamb * xnew[1], 0]
    xnew[2] = f(xnew[0], xnew[1])
    print("xnew:", xnew)

    if (f(x[0], x[1]) > f(xnew[0], xnew[1])):
        lamb *= 2
    else:
        lamb /= 2

    xold = x.copy()
    x = xnew.copy()

print("result:", x)
