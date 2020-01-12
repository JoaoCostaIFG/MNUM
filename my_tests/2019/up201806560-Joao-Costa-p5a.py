#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p5a.py

# we'll call dy/dt, z
# so we get a new expression and
# the given expression becomes:
# dz/dt = A + t^2 + t * z

A = 1.5

def dydt(t, y, z):
    return z

def dzdt(t, y, z):
    return A + (t**2) + t * z

    
# s
t = 1
y = 0
z = 1  # y'0
h = 0.2
n = 2
print("n:", 0, "t:", t, "y:", y, "z:", z)
for i in range(n):
    z += dzdt(t, y, z) * h
    y += dydt(t, y, z) * h
    t += h
    print("n:", i+1, "t:", t, "y:", y, "z:", z)