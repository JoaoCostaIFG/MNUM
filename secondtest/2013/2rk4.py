#!/usr/bin/env python3

# CHECKED

from math import sin


def f(x, t):
    return sin(2 * x) + sin(2 * t)


x = 1
t = 1
xf = 1.5
deltax = 0.125
while x < xf:
    delta1 = deltax * f(x, t)
    delta2 = deltax * f(x + deltax/2, t + delta1/2)
    delta3 = deltax * f(x + deltax/2, t + delta2/2)
    delta4 = deltax * f(x + deltax, t + delta3)

    deltat = delta1/6 + delta2/3 + delta3/3 + delta4/6
    t += deltat
    x += deltax
    print("x:", x, "t:", t)
s = t

x = 1
t = 1
xf = 1.5
deltax = 0.125 / 2
while x < xf:
    delta1 = deltax * f(x, t)
    delta2 = deltax * f(x + deltax/2, t + delta1/2)
    delta3 = deltax * f(x + deltax/2, t + delta2/2)
    delta4 = deltax * f(x + deltax, t + delta3)

    deltat = delta1/6 + delta2/3 + delta3/3 + delta4/6
    t += deltat
    x += deltax
print("x:", x, "t:", t)
sl = t


x = 1
t = 1
xf = 1.5
deltax = 0.125 / 4
while x < xf:
    delta1 = deltax * f(x, t)
    delta2 = deltax * f(x + deltax/2, t + delta1/2)
    delta3 = deltax * f(x + deltax/2, t + delta2/2)
    delta4 = deltax * f(x + deltax, t + delta3)

    deltat = delta1/6 + delta2/3 + delta3/3 + delta4/6
    t += deltat
    x += deltax
print("x:", x, "t:", t)
sll = t

kc = (sl - s) / (sll - sl)
print("kc:", kc)
