#!/usr/bin/env python3

# 1)
# Solved in maxima
# a: 2;
# b: 60;
# g: - x + b * cos(sqrt(x)) + a;
# plot2d(g, [x, -10, 1000]);
# The function has 3 roots.

# 2)
# In maxima: diff(g, x);

from math import sqrt, sin, cos

a = 2
b = 60


def g(x):
    return -x + b * cos(sqrt(x)) + a


def dg(x):
    return -1 - 30 * sin(sqrt(x)) / sqrt(x)


x = 1.8
print(x, g(x))
for i in range(3):
    x -= g(x) / dg(x)
    print(x, g(x))


# 3)
# In the low amount of iterations we did, we got 2 iterations where the first decimal place was stable (didn't change).
# This didn't happen so for the second decimal place so it doesn't matter after that one.
# With this, we can say that the calculations we did provided us with 1 exact decimal place.
# Answer: 1
