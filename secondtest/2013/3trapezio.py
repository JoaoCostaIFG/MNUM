#!/usr/bin/env python3

# CHECKED

from math import e, sqrt

k = 1.5


def f(x):
    return sqrt(1 + ((k * e ** (k * x)) ** 2))


# first 2 are the same shit but first one is better (not in texto tho)
a = 0
b = 1
h = 0.25
n = 4
trap = f(a) + f(b)
for i in range(1, n):
    trap += 2 * f(a + i * h)
trap *= (h / 2)
print(trap)

a = 0
b = 1
h = 0.25
n = 4
trap = (f(a) + f(b)) / 2
for i in range(1, n):
    trap += f(a + i * h)
trap *= h
print(trap)

a = 0
b = 1
h = 0.25 / 2
n = 8
trap = (f(a) + f(b)) / 2
for i in range(1, n):
    trap += f(a + i * h)
trap *= h
print(trap)

a = 0
b = 1
h = 0.25 / 4
n = 16
trap = (f(a) + f(b)) / 2
for i in range(1, n):
    trap += f(a + i * h)
trap *= h
print(trap)
