#!/usr/bin/env python3

import math
from time import sleep


def g(x):
    return -(0.660 * x - 1) / (x - 1) + x


def gl(x):
    temp = 50 * x**2 - 100 * x
    return (temp + 33) / (temp + 50)


ERRR = 1e-10
x_old = False
x = 1.67

while (abs(x - x_old) > ERRR):
    print("x:", x)
    print("gl:", gl(x))
    print()
    x_old = x
    x = g(x)
    # sleep(1)

print("Final:", x)
