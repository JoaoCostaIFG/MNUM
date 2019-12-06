#!/usr/bin/env python3

# Checked

from math import e


a = 15
b = 0.1


def dCdt(t, C, T):
    return C * -e ** (-b/(T + 273))


def dTdt(t, C, T):
    return a * C * e ** (-b/(T + 273)) - b * (T - 20)


t = 0.5
C = 2
T = 20
h = 0.25
print("h, t, C, T")
print(h, t, C, T)
for i in range(2):
    d1C = h * dCdt(t, C, T)
    d1T = h * dTdt(t, C, T)

    d2C = h * dCdt(t + h/2, C + d1C/2, T + d1T/2)
    d2T = h * dTdt(t + h/2, C + d1C/2, T + d1T/2)

    d3C = h * dCdt(t + h/2, C + d2C/2, T + d2T/2)
    d3T = h * dTdt(t + h/2, C + d2C/2, T + d2T/2)

    d4C = h * dCdt(t + h/2, C + d3C, T + d3T)
    d4T = h * dTdt(t + h/2, C + d3C, T + d3T)

    t += h
    C += d1C/6 + d2C/3 + d3C/3 + d4C/6
    T += d1T/6 + d2T/3 + d3T/3 + d4T/6
    print(h, t, C, T)
