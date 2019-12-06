#!/usr/bin/env python3

from math import sin, pi

def f(x):
    # return x**3
    return x**2 * sin(x)


def integral(x, y):
    return x + y


def qc(a, b, n, f, metodo, ordem):
    s = metodo(a, b, n, f)
    sl = metodo(a, b, n * 2, f)
    sll = metodo(a, b, n * 4, f)

    qc = (sl - s) / (sll - sl)
    print("QC:", qc)

    error(ordem, sll, sl)
    return qc


def error(ordem, sll, sl):
    error = (sll - sl) / (2**ordem - 1)
    print("Error:", error)
    return error


def trap(a, b, n, f):  # ordem 4
    h = (b - a) / n
    summ = 0

    for i in range(1, n):
        summ += 2 * f(a + i * h)

    summ += f(a) + f(b)
    summ *= (h/2)

    print("Trapezio result:", summ)
    return summ


def simpson(a, b, n, f):  # ordem 2
    summ = (f(a) + f(b))
    dx = (b - a) / n

    temp_summ = 0
    for i in range(1, n, 2):
        temp_summ += f(a + i * dx)
    summ += (4 * temp_summ)

    temp_summ = 0
    for i in range(2, n - 1, 2):
        temp_summ += f(a + i * dx)
    summ += (2 * temp_summ)

    summ *= (dx / 3)
    print("Simpson result:", summ)
    return summ


def simpson_duplo(a, b, n, f, const):  # ordem 2
    summ = (f(const, a) + f(const, b))
    dx = (b - a) / n

    temp_summ = 0
    for i in range(1, n, 2):
        temp_summ += f(const, a + i * dx)
    summ += (4 * temp_summ)

    temp_summ = 0
    for i in range(2, n - 1, 2):
        temp_summ += f(const, a + i * dx)
    summ += (2 * temp_summ)

    summ *= (dx / 3)
    print("Simpson result:", summ)
    return summ


# qc(0, pi/2, 200, f, trap, 4)
# print()
# qc(0, pi/2, 200, f, simpson, 2)
# print('\n')
n = 100
summ = simpson_duplo(0, 1, n, integral, 0)
for i in range(1, n):
    summ += 4 * simpson_duplo(0, 1, n, integral, 0 + (1 - 0)/n * i)
summ += simpson_duplo(0, 1, n, integral, 1)
summ *= (1 - 0)/n/3
print("Result integral duplo:", summ)
