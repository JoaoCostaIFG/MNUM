#!/usr/bin/env python3

# CHECKED

from math import e


def f1(t, C, T):
    return -e ** (-0.5 / (T + 273)) * C


def f2(t, C, T):
    return 20 * e ** (-0.5 / (T + 273)) * C - 0.5 * (T - 20)


t = 0
deltat = 0.2
C = 2
T = 20
for i in range(2):
    t_new = t + deltat
    T_new = T + f2(t, C, T) * deltat
    C_new = C + f1(t, C, T) * deltat
    t = t_new
    T = T_new
    C = C_new
print(t, C, T)

t = 0
deltat = 0.2 / 2
C = 2
T = 20
for i in range(4):
    t_new = t + deltat
    T_new = T + f2(t, C, T) * deltat
    C_new = C + f1(t, C, T) * deltat
    t = t_new
    T = T_new
    C = C_new
print(t, C, T)

t = 0
deltat = 0.2 / 4
C = 2
T = 20
for i in range(8):
    t_new = t + deltat
    T_new = T + f2(t, C, T) * deltat
    C_new = C + f1(t, C, T) * deltat
    t = t_new
    T = T_new
    C = C_new
print(t, C, T)
