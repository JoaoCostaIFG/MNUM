#!/usr/bin/env python3

# CHECKED

def f(x, y):
    return -0.25 * (y - Ta)


h = 0.4
ti = 1
#  tf = 1 + 2*h
Ti = 23
Ta = 45

for i in range(2):
    print(ti, Ti)
    deltax = h
    deltay = f(ti, Ti) * deltax
    ti = ti + deltax
    Ti = Ti + deltay

print(ti, Ti)
