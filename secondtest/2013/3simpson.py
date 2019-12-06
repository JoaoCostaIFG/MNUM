#!/usr/bin/env python3

# CHECKED

from math import e, sqrt

k = 1.5


def f(x):
    return sqrt(1 + ((k * e ** (k * x)) ** 2))


a = 0
b = 1
h = 0.25
n = 4
trap = f(a) + f(b)
for i in range(1, n, 2):
    trap += 4 * f(a + h * i)
for i in range(2, n - 1, 2):
    trap += 2 * f(a + h * i)
trap *= (h / 3)
print(trap)


a = 0
b = 1
h = 0.25 / 2
n = 8
trap = f(a) + f(b)
for i in range(1, n, 2):
    trap += 4 * f(a + h * i)
for i in range(2, n - 1, 2):
    trap += 2 * f(a + h * i)
trap *= (h / 3)
print(trap)

a = 0
b = 1
h = 0.25 / 4
n = 16
trap = f(a) + f(b)
for i in range(1, n, 2):
    trap += 4 * f(a + h * i)
for i in range(2, n - 1, 2):
    trap += 2 * f(a + h * i)
trap *= (h / 3)
print(trap)
