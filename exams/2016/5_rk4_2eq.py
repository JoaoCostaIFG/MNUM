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
    d1y = h * dydt(t, y, z)
    d1z = h * dzdt(t, y, z)

    d2y = h * dydt(t + h / 2, y + d1y / 2, z + d1z / 2)
    d2z = h * dzdt(t + h / 2, y + d1y / 2, z + d1z / 2)

    d3y = h * dydt(t + h / 2, y + d2y / 2, z + d2z / 2)
    d3z = h * dzdt(t + h / 2, y + d2y / 2, z + d2z / 2)

    d4y = h * dydt(t + h, y + d3y, z + d3z)
    d4z = h * dzdt(t + h, y + d3y, z + d3z)

    t += h
    y += d1y / 6 + d2y / 3 + d3y / 3 + d4y / 6
    z += d1z / 6 + d2z / 3 + d3z / 3 + d4z / 6
    print(t, y, z)
