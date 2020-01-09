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
    nT = T + dTdt(t, C, T) * h
    nC = C + dCdt(t, C, T) * h
    t += h
    T = nT
    C = nC
    print("t:", t, "C:", C, "T:", T)
