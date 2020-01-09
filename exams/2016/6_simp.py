#!/usr/bin/env python3

from math import sqrt, e

k = 1.5


def f(x):
    return sqrt(1 + (k * e**(k * x))**2)


def simp(a, b, h):
    n = int((b - a) / h)
    simp = f(a) + f(b)
    for i in range(1, n, 2):
        simp += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        simp += 2 * f(a + i * h)
    return h / 3 * simp


a = 0
b = 2
h = 0.5
s = simp(a, b, h)
print("s:", s)
sl = simp(a, b, h / 2)
print("sl:", sl)
sll = simp(a, b, h / 4)
print("sll:", sll)

qc = (sl - s) / (sll - sl)
erro = (sll - sl) / (2**4 - 1)
print("qc:", qc, "err:", erro)
