#!/usr/bin/env python3

from math import e, sqrt

k = 2.5


def f(x):
    return sqrt(1 + (k * e**(k * x))**2)


# S
a = 0
b = 1
h = 0.125
n = int((b - a) / h)
s = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + i * h)
s += 4 * temp

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + i * h)
s += 2 * temp

s *= (h / 3)
print("s:", s)

# Sl
a = 0
b = 1
h = 0.125 / 2
n = int((b - a) / h)
sl = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + i * h)
sl += 4 * temp

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + i * h)
sl += 2 * temp

sl *= (h / 3)
print("sl:", sl)

# Sll
a = 0
b = 1
h = 0.125 / 4
n = int((b - a) / h)
sll = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + i * h)
sll += 4 * temp

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + i * h)
sll += 2 * temp

sll *= (h / 3)

print("sll:", sll)

# QC
qc = (sl - s) / (sll - sl)
print("QC:", qc)
# ERR
erro = (sll - sl) / (2**2 - 1)
print("err:", erro)
