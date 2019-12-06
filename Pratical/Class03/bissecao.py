#!/usr/bin/env python3


def formula_resolvente1(a, b, c):
    return (-b - (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def formula_resolvente2(a, b, c):
    return (-b + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def expr(x):
    return 2 * x**2 - 5 * x - 2


def bissec(x, a, b, p):
    print("Root:", x)
    print("Erro absoluto max:", abs(b - a)/2)

    medio = (a + b) / 2
    while abs(b - a) > p:
        medio = (a + b) / 2

        if (expr(medio) * expr(a) <= 0):
            b = medio

        else:
            a = medio

    print("Result:", medio)
    print("Erro absoluto:", x - medio)

    return medio


bissec(formula_resolvente1(2, -5, -2), -1, 0, 1e-10)
print()
bissec(formula_resolvente2(2, -5, -2), 2, 3, 1e-10)
