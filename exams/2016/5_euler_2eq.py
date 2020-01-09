#!/usr/bin/env python3

A = 0.5


def dydt(t, y, z):
    return z


def dzdt(t, y, z):
    return A + t**2 + t * z


t = 0
y = 0
z = 1
h = 0.25
for i in range(2):
    ny = dydt(t, y, z) * h
    nz = dzdt(t, y, z) * h

    t += h
    y += ny
    z += nz
    print(t, y, z)
