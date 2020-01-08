#!/usr/bin/env python3

from math import log, e


def f(x):
    return (e**x) - (4 * (x * x))


def recorr(x):
    return 2 * log(2 * x)


# only 1 iteration to calculate
x = 1.1
print(x)
x = recorr(x)
print(x)


#
# (DON'T DO THIS, IT IS INCORRECT)
#
# Residue (how much is left to an equation for it to become an identity)
print("Residue:", 0 - f(x))  # not sure why this is not correct
