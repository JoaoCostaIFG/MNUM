#!/usr/bin/env python3

from math import sqrt, e

k = 1.5


def f(x):
    return sqrt(1 + (k * e**(k * x))**2)


def trap(a, b, h):
    n = int((b - a) / h)
    trap = f(a) + f(b)
    for i in range(1, n):
        trap += 2 * f(a + i * h)
    return h / 2 * trap


a = 0
b = 2
h = 0.5
s = trap(a, b, h)
print("s:", s)
sl = trap(a, b, h / 2)
print("sl:", sl)
sll = trap(a, b, h / 4)
print("sll:", sll)

qc = (sl - s) / (sll - sl)
erro = (sll - sl) / (2**2 - 1)
print("qc:", qc, "err:", erro)
