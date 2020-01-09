#!/usr/bin/env python3

a = 1
b = 0.5
c = 0.5


def f(x):
    return a * x**7 + b * x - c


xe = 0  # xe
xd = 0.8  # xd
xn = 0.656044
# dados: f(xe) * f(xn) >= 0
xe = xn
xn = (xe * f(xd) - xd * f(xe)) / (f(xd) - f(xe))
print("xe:", xe, "xd:", xd, "xn:", xn)

for i in range(2):

    if (f(xe) * f(xn) < 0):
        b = xn
    else:
        xe = xn
    xn = (xe * f(xd) - xd * f(xe)) / (f(xd) - f(xe))

    print("xe:", xe, "xd:", xd, "xn:", xn)

"""
b)
1 - Fundamental
2 - nao se aplica
3 - Aplica-se
4 - Aplica-se
"""
