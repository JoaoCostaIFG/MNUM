#!/usr/bin/env python

from math import sqrt, e

k = 2.5


def f(x):
    return sqrt(1 + (k * e**(k * x))**2)


def trap(a, b, h):
    n = int((b - a) / h)
    trap = f(a) + f(b)

    for i in range(1, n):
        trap += 2 * f(a + i * h)

    trap *= (h / 2)
    print(trap)
    return trap


a = 0
b = 1
h = 0.125

# s
s = trap(a, b, h)
# sl
sl = trap(a, b, h / 2)
# sll
sll = trap(a, b, h / 4)

# QC
qc = (sl - s) / (sll - sl)
# err
erro = (sll - sl) / (2**2 - 1)

print("QC:", qc)
print("err:", abs(erro))
