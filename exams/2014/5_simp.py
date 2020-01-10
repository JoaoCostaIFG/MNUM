#!/usr/bin/env python

from math import sqrt, e

k = 2.5


def f(x):
    return sqrt(1 + (k * e**(k * x))**2)


def simp(a, b, h):
    n = int((b - a) / h)
    simp = f(a) + f(b)

    for i in range(1, n, 2):
        simp += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        simp += 2 * f(a + i * h)

    simp *= (h / 3)
    print(simp)
    return simp


a = 0
b = 1
h = 0.125

# s
s = simp(a, b, h)
# sl
sl = simp(a, b, h / 2)
# sll
sll = simp(a, b, h / 4)

# QC
qc = (sl - s) / (sll - sl)
# err
erro = (sll - sl) / (2**4 - 1)

print("QC:", qc)
print("err:", abs(erro))
