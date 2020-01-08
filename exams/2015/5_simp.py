#!/usr/bin/env python3

from math import sqrt, e

k = 2.5


def f(x):
    return sqrt(1 + (k * e**(k*x))**2)


# S
a = 0
b = 1
h = 0.125
n = int((b - a) / h)
simp = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + h * i)
simp += temp * 4

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + h * i)
simp += temp * 2

simp *= h/3
print("simp s:", simp)
s = simp


# Sl
a = 0
b = 1
h = 0.125 / 2
n = int((b - a) / h)
simp = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + h * i)
simp += temp * 4

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + h * i)
simp += temp * 2

simp *= h/3
print("simp sl:", simp)
sl = simp


# Sll
a = 0
b = 1
h = 0.125 / 4
n = int((b - a) / h)
simp = f(a) + f(b)

temp = 0
for i in range(1, n, 2):
    temp += f(a + h * i)
simp += temp * 4

temp = 0
for i in range(2, n - 1, 2):
    temp += f(a + h * i)
simp += temp * 2

simp *= h/3
print("simp sll:", simp)
sll = simp


# QC
qc = (sl - s) / (sll - sl)
print("QC:", qc)
# erro
erro = (sll - sl) / (2**4 - 1)
print("erro:", erro)
