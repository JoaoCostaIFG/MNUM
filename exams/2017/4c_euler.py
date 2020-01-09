#!/usr/bin/env python3

from math import e

a = 30
b = 0.5


def dCdt(t, C, T):
    return -e**(-b / (T + 273)) * C


def dTdt(t, C, T):
    return a * e**(-b / (T + 273)) * C - b * (T - 20)


tf = 0.5


def euler(h):
    t = 0
    C = 2.5
    T = 25
    while (t < tf):
        nT = T + dTdt(t, C, T) * h
        nC = C + dCdt(t, C, T) * h
        t += h
        T = nT
        C = nC
        print("t:", t, "C:", C, "T:", T)

    return T


h = 0.25
s = euler(h)
sl = euler(h / 2)
sll = euler(h / 4)
print("s:", s, "sl", sl, "sll", sll)

# QC
qc = (sl - s) / (sll - sl)
print("QC:", qc)

# ERR
erro = (sll - sl) / (2**1 - 1)
print("err:", erro)
