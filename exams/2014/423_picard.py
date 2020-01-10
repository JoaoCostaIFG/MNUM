#!/usr/bin/env python3

from math import log


def recorr(x):
    return 2 * log(2 * x)


x = 1.1
print(x)
x = recorr(x)
print(x)

# Residue
print(x - 1.1)  # x1 - x0
