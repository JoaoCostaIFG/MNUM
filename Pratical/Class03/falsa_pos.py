#!/usr/bin/env python3


def formula_resolvente1(a, b, c):
    return (-b - (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def formula_resolvente2(a, b, c):
    return (-b + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)


def expr(x):
    return 2 * x**2 - 5 * x - 2


def falsa_pos(x, a, b, p):
    print("root:", x)
    print("erro absoluto max:", abs(b - a)/2)
    print()

    medio = (a * expr(b) - b * expr(a)) / (expr(b) - expr(a))
    while abs(x - medio) > p:
        medio = (a * expr(b) - b * expr(a)) / (expr(b) - expr(a))

        if (expr(medio) * expr(a) <= 0):
            b = medio

        else:
            a = medio

    print("result:", medio)
    print("erro absoluto:", x - medio)

    return medio


falsa_pos(formula_resolvente1(2, -5, -2), -1, 0, 1e-10)
print("\n")
falsa_pos(formula_resolvente2(2, -5, -2), 2, 3, 1e-10)
