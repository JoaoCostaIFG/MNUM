#!/usr/bin/env python3

from math import sin

a = 1
b = 2


def dxdt(t, x):
    return sin(a * x) + sin(b * t)


def rk4(t, x, tf, h):
    print("h:", h)
    print("t:", t, "x:", x)
    while (t < tf):
        d1 = h * dxdt(t, x)
        d2 = h * dxdt(t + h / 2, x + d1 / 2)
        d3 = h * dxdt(t + h / 2, x + d2 / 2)
        d4 = h * dxdt(t + h, x + d3)

        x += d1 / 6 + d2 / 3 + d3 / 3 + d4 / 6
        t += h
        print("t:", t, "x:", x)

    return x


t = 1
x = 0
tf = 1.5
h = 0.5
s = rk4(t, x, tf, h)
print("s:", s)
sl = rk4(t, x, tf, h / 2)
print("sl:", sl)
sll = rk4(t, x, tf, h / 4)
print("sll:", sll)

# QC
qc = (sl - s) / (sll - sl)
print("QC:", qc)

# Err
erro = (sll - sl) / (2**4 - 1)
print("err:", erro)

#  c)
#  For the RK4 we expect to get a QC of around 16. Our QC value is too high so we should decrease ourstep: h''/2 = 0.0625 should be the value of our step, h.
