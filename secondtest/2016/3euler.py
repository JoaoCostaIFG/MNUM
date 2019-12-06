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
t_end = 1
h = 0.25
print("h, t, C, T")
print(h, t, C, T)
while (t < t_end):
    C_new = h * dCdt(t, C, T)
    T_new = h * dTdt(t, C, T)
    t += h
    C += C_new
    T += T_new
    print(h, t, C, T)
s = C

t = 0.5
C = 2
T = 20
t_end = 1
h = 0.1250
print("h, t, C, T")
print(h, t, C, T)
while (t < t_end):
    C_new = h * dCdt(t, C, T)
    T_new = h * dTdt(t, C, T)
    t += h
    C += C_new
    T += T_new
    print(h, t, C, T)
sl = C

t = 0.5
C = 2
T = 20
t_end = 1
h = 0.0625
print("h, t, C, T")
print(h, t, C, T)
while (t < t_end):
    C_new = h * dCdt(t, C, T)
    T_new = h * dTdt(t, C, T)
    t += h
    C += C_new
    T += T_new
    print(h, t, C, T)
sll = C

print("Ch' Ch''")
print(sl, sll)

qc = (sl - s) / (sll - sl)
print("QC:", qc)

err = (sll - sl) / 1
print("Err:", err)
