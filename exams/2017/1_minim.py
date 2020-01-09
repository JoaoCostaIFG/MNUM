#!/usr/bin/env python3
"""
We can use one of the following methods: thirds method, golden rule method or
quadractic interpolation method.
We'll use the golden rule method.

Using maxima:
a: 0;
eq:(x - a)**2 + x**4;
plot2d(eq, [x, -5, 5]);

By obeservation of the graph, we can see that the function has at
least 1 minimum at (-5, 5)
"""

from math import sqrt

a = 0  # last digit of my up student number


def f(x):
    return (x - a)**2 + x**4


def init_search(guess, step):
    if f(guess) < f(guess + step):
        step *= -1

    a = guess + step
    b = guess + 2 * step
    while f(a) > f(b):
        a = b
        b += step

    print("init search:", a, b)
    return (a, b)


def aurea(xi, xf, erro):
    print("Aurea:")
    B = (sqrt(5) - 1) / 2  # golden ratio
    A = B**2

    x3 = xi + A * (xf - xi)
    x4 = xi + B * (xf - xi)
    while abs(xi - xf) > erro:
        if f(x4) < f(x3):
            xi = x3
            x3 = x4

            x4 = x3 + B * (xf - x3)
        elif f(x3) <= f(x4):
            xf = x4
            x4 = x3

            x3 = xi + B * (xf - xi)

    print("xi:", xi, "xf:", xf)
    print("fi:", f(xi), "ff:", f(xf))
    return (xi, xf)


aurea(*init_search(1, 0.01), 0.001)
