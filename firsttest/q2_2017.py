#!/usr/bin/env python3

r = float(input("R: "))
m = float(input("m: "))


def expr(x):
    return (x**m - r) / (m * x ** (m - 1))


iter = 23
x = 3

for i in range(0, iter):
    x = x - expr(x)


print(x)
