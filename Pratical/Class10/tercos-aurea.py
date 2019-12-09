#!/usr/bin/env python3

# These methods won't be on the 2nd mini test (no algorithm implementation)
# so I will verify if they are correct after the test
# (should at least be really close to correct)

from math import sin, sqrt

limm = 1e-5


def f(x):
    return sin(x) ** 2


def const_search(xi, xf, h):
    print("const_search")
    # change direc if necessary
    if (f(xi) < f(xi + h)):
        h = -h

    while f(xi) > f(xi + h):
        xi += h

    print("xi:", xi, "h:", h)
    return xi


def inc_search(xi, xf, h):
    print("inc_search")
    # change direc if necessary
    if (f(xi) < f(xi + h)):
        h = -h

    while f(xi) > f(xi + h):
        h *= 2
        xi += h

    print("xi:", xi, "h:", h)
    return xi


def adjust(xi, xf, xm):
    # Adjust 3 points to parabola
    result = xf + ((xm - xf) * (f(xi) - f(xm))) / \
        (2 * (f(xm) - 2 * f(xf) + f(xi)))
    print(result)
    return result


def tercos(xi, xf):
    # doing 10 iterations cause it seems OK for this problem
    print("Tercos:")
    lastx = 0
    for i in range(10):
        h = (xf - xi) / 3
        x3 = xi + h
        x4 = xf - h
        if f(x4) < f(x3):
            xi = x3
            lastx = x4
        elif f(x3) <= f(x4):
            # TODO caso do ==
            # podemos abandonar ambos os extremos do intervalo
            xf = x4
            lastx = x3

    print("xi:", xi, "xf:", xf)
    print("fi:", f(xi), "ff:", f(xf))
    return (xi, xf, lastx)


def aurea(xi, xf):
    # doing 10 iterations cause it seems OK for this problem
    print("Aurea:")
    B = (sqrt(5) - 1) / 2  # golden ratio
    A = B ** 2

    lastx = 0
    x3 = xi + A * (xf - xi)
    x4 = xi + B * (xf - xi)
    for i in range(10):
        if f(x4) < f(x3):
            xi = x3
            lastx = x3 = x4

            x4 = x3 + B * (xf - x3)
        elif f(x3) <= f(x4):
            xf = x4
            lastx = x4 = x3

            x3 = xi + B * (xf - xi)

    print("xi:", xi, "xf:", xf)
    print("fi:", f(xi), "ff:", f(xf))
    return (xi, xf, lastx)


# f is convex from -1 to 1
xi = -1
xf = 1
h = 0.1
# tercos
xi = const_search(xi, xf, h)
points = tercos(xi, xf)
result = adjust(*points)  # the star (*) unpacks the sequence

# f is convex from -1 to 1
xi = -1
xf = 1
h = 0.1
# aurea
xi = const_search(xi, xf, h)
points = aurea(xi, xf)
result = adjust(*points)  # the star (*) unpacks the sequence
