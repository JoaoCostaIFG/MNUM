#!/usr/bin/env python3

Ta = 37


def dTdt(t, T):
    return -0.25 * (T - Ta)


t = 5
T = 3
h = 0.4  # aka delta_x
for i in range(2):
    t += h
    delta_T = dTdt(t, T) * h  # aka delta_y
    T += delta_T

print(t, T)
