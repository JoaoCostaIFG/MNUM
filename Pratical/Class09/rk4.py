#!/usr/bin/env python3

import math
import matplotlib.pyplot as plt


def f(x, y):
    return math.pow(math.sin(x), 2)


def qc(a, b, h, f, xn, metodo):
    s = metodo(a, b, h, f, xn)
    sl = metodo(a, b, h/2, f, xn)
    sll = metodo(a, b, h/4, f, xn)

    print("qc\nerro")
    qc = []
    for i in range(len(s)):
        numerator = sll[i*4][1] - sl[i*2][1]
        if numerator == 0:
            qc.append("div by 0")
            print(qc[i])
            continue
        else:
            qc.append((sl[i*2][1] - s[i][1]) / numerator)

        print(qc[i], abs(qc[i] - 16))
        print()

    plt.show()
    return qc


def rk4(x, y, dltx, f, xf, doplot=True):
    points = [(x, y)]

    while (x < xf):
        x += dltx
        dlt1 = dltx * f(x, y)
        dlt2 = dltx * f(x + dltx/2, y + dlt1/2)
        dlt3 = dltx * f(x + dltx/2, y + dlt2/2)
        dlt4 = dltx * f(x + dltx, y + dlt3)
        y += dlt1/6 + dlt2/3 + dlt3/3 + dlt4/6  # y += y + dlty
        points.append((x, y))

    if doplot:
        x, y = zip(*points)
        plt.scatter(x, y, marker=".")

    return points


h = 0.01
x = 0
y = 0
xf = 100
qc(x, y, h, f, xf, rk4)
#  rk4(x, y, h, xf, f, True)
