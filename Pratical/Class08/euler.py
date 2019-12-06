#!/usr/bin/env python3

import matplotlib.pyplot as plot


def df(x, y):
    return x


def qc(a, b, h, f, xn, metodo):
    s = metodo(a, b, h, f, xn)
    sl = metodo(a, b, h/2, f, xn)
    sll = metodo(a, b, h/4, f, xn)

    print("x        y        yl        yll        qc        erro")
    qc = []
    for i in range(len(s)):
        numerator = sll[i*4][1] - sl[i*2][1]
        if numerator == 0:
            qc.append("div by 0")
        else:
            qc.append((sl[i*2][1] - s[i][1]) / numerator)

        # print(s[i][0], s[i][1] sl[i*2][1], sll[i*4][1], qc[i])

    return qc


def euler(x, y, h, df, xn, doplot=False):
    points = []
    points.append((x, y))

    while x < xn:
        delx = h
        dely = df(x, y) * delx
        y = y + dely
        x = x + delx

        points.append((x, y))

    if doplot:
        x, y = zip(*points)
        plot.scatter(x, y)
        plot.show()

    return points


x0 = 0
y0 = 1
h = 1
xn = 50

qc(x0, y0, h, df, xn, euler)
