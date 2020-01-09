#!/usr/bin/env python3

from math import e

a = 30
b = 0.5


def dCdt(t, C, T):
    return -e**(-b / (T + 273)) * C


def dTdt(t, C, T):
    return a * e**(-b / (T + 273)) * C - b * (T - 20)


t = 0
C = 2.5
T = 25
h = 0.25
for i in range(2):
    d1C = h * dCdt(t, C, T)
    d1T = h * dTdt(t, C, T)

    d2C = h * dCdt(t + h/2, C + d1C/2, T + d1T/2)
    d2T = h * dTdt(t + h/2, C + d1C/2, T + d1T/2)

    d3C = h * dCdt(t + h/2, C + d2C/2, T + d2T/2)
    d3T = h * dTdt(t + h/2, C + d2C/2, T + d2T/2)

    d4C = h * dCdt(t + h, C + d3C, T + d3T)
    d4T = h * dTdt(t + h, C + d3C, T + d3T)

    t += h
    C += d1C/6 + d2C/3 + d3C/3 + d4C/6
    T += d1T/6 + d2T/3 + d3T/3 + d4T/6
    print("t:", t, "C:", C, "T:", T)
