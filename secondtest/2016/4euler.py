#!/usr/bin/env python3

# Checked

Ta = 64


def dTdt(t, T):
    return -0.25 * (T - Ta)


t = 4
T = 0
h = 0.5
print("h, t, T")
print(h, t, T)
for i in range(2):
    T += h * dTdt(t, T)
    t += h
    print(h, t, T)
