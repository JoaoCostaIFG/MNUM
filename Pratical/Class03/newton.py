#!/usr/bin/env python3

from time import sleep


def formula_resolvente1(a, b, c):
    return (-b - (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def formula_resolvente2(a, b, c):
    return (-b + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def expr(x):
    # 2x^2 - 5x - 2
    return 2 * x**2 - 5 * x - 2


def derivative(x):
    # 4x - 5
    return 4 * x - 5


def simplified(x):
    # (2x^2 + 2) / (4x - 5)
    return (x**2 + 1) / (2 * x - 2.5)


def newton(s, x, p):
    print("root:", s)
    # print("erro absoluto max:", abs(b - a) / 2)
    print()

    while abs(x - s) > p:
        # x = x - (expr(x) / derivative(x))
        x = simplified(x)
        print("Erro:", abs(x - s))

    print("result:", x)
    print("erro absoluto:", x - s)

    return x


newton(formula_resolvente1(2, -5, -2), -1, 1e-10)
print("\n")
newton(formula_resolvente2(2, -5, -2), 2, 1e-10)
