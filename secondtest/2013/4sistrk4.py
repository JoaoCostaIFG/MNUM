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
    delta1 = deltat * f1(t, C, T)
    delta1_2 = deltat * f2(t, C, T)

    delta2 = deltat * f1(t + deltat/2, C + delta1/2, T)
    delta2_2 = deltat * f2(t + deltat/2, C, T + delta1_2/2)

    delta3 = deltat * f1(t + deltat/2, C + delta2/2, T)
    delta3_2 = deltat * f2(t + deltat/2, C, T + delta2_2/2)

    delta4 = deltat * f1(t + deltat, C + delta3, T)
    delta4_2 = deltat * f2(t + deltat, C, T + delta3)

    t += deltat
    C += delta1/6 + delta2/3 + delta3/3 + delta4/6
    T += delta1_2/6 + delta2_2/3 + delta3_2/3 + delta4_2/6

print(t, C, T)
