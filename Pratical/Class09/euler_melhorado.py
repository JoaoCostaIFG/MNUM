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


def euler_helper(x, y, x2, y2, dltx, step):
    dltx /= step
    for i in range(step):
        yl = f(x2, y2)
        pn = y + 2 * yl * dltx
        pln = f(x2, pn)
        dlty = (pln + yl) / 2 * dltx

        x = x2
        y = y2
        x2 = x + dltx
        y2 = y + dlty

    return y



def euler_melhorado(x, y, x2, y2, dltx, f, xf, doplot=True):
    points = [(x, y)]
    while (x < xf):
        yl = f(x2, y2)
        pn = y + 2 * yl * dltx
        pln = f(x2, pn)
        dlty = (pln + yl) / 2 * dltx

        sll = euler_helper(x, y, x2, y2, dltx, 4)
        sl = euler_helper(x, y, x2, y2, dltx, 2)
        numerator = sl - (y2 + dlty)
        if numerator:
            kc = (sll - sl) / (sl - (y2 + dlty))
        else:
            kc = 2
        if (abs(kc - 2) < 8):
            x = x2
            y = y2
            x2 = x + dltx
            y2 = y + dlty
            points.append((x, y))
        else:
            dltx -= 0.1

    if doplot:
        x, y = zip(*points)
        plt.scatter(x, y, marker=".")

    return points


x = 0
y = 0
rk4res = rk4(x, y, 0.001, f, 1, False)
x2 = rk4res[-1][0]
y2 = rk4res[-1][1]
h = 1
xf = 20
euler_melhorado(x, y, x2, y2, h, f, xf, True)
plt.show()
