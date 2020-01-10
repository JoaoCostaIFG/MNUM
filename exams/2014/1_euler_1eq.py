#!/usr/bin/env python3

Ta = 37


def dTdt(t, T):
    return -0.25 * (T - Ta)


t = 5
T = 3
h = 0.4

for i in range(2):
    T += h * dTdt(t, T)
    t += h
    print(t, T)
