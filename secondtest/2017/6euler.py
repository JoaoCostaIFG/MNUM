#!/usr/bin/env python3

# CHECKED

A = 2


def f1(t, y, z):
    return A + t**2 + t * z


def f2(t, y, z):
    return z


deltat = 0.25
t = 1
y = 1
z = 0
print(t, y, z)
for i in range(10):
    t_new = t + deltat
    y_new = y + f2(t, y, z) * deltat
    z_new = z + f1(t, y, z) * deltat

    t = t_new
    y = y_new
    z = z_new
    print(t, y, z)
