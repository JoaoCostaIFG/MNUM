#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p5b.py

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
    d1y = h * dydt(t, y, z)
    d1z = h * dzdt(t, y, z)
    
    d2y = h * dydt(t + h/2, y + d1y/2, z + d1z/2)
    d2z = h * dzdt(t + h/2, y + d1y/2, z + d1z/2)
    
    d3y = h * dydt(t + h/2, y + d2y/2, t + d2z/2)
    d3z = h * dzdt(t + h/2, y + d2y/2, t + d2z/2)

    d4y = h * dydt(t + h, y + d3y, z + d3z)    
    d4z = h * dzdt(t + h, y + d3y, z + d3z)

    y += d1y/6 + d2y/3 + d3y/3 + d4y/6
    z += d1z/6 + d2z/3 + d3z/3 + d4z/6
    t += h
    
    print("n:", i+1, "t:", t, "y:", y, "z:", z)