#!/usr/bin/env python3

# CHECKED

# Second-order ODE solved using rk4 method
# y'' = A + t^2 + t * y'
# Initial values:
# t0 = 1, y0 = 1, y0' = 0
# Based on the given equation, we say:
# z' = A + t^2 + t * z
# y' = z
A = 2


def dzdt(t, y, z):
    # z' = A + t^2 + t * z
    return A + t**2 + t * z


def dydt(t, y, z):
    # y' = z
    return z


def rk4_vil(t, y, z, h, n=10):
    # Villate style (diferente do TEXTO)
    # NOTE: In MAXIMA we can use this command to check our solution:
    # rk([2 + t * t + t * z, z], [z, y], [0, 1], [t, 1, 4, 0.25]);
    print("Villate\nt y z")
    print(t, y, z)
    for i in range(n):
        d1y = dydt(t, y, z)
        d1z = dzdt(t, y, z)

        d2y = dydt(t + h/2, y + (h/2) * d1y, z + (h/2) * d1z)
        d2z = dzdt(t + h/2, y + (h/2) * d1y, z + (h/2) * d1z)

        d3y = dydt(t + h/2, y + (h/2) * d2y, z + (h/2) * d2z)
        d3z = dzdt(t + h/2, y + (h/2) * d2y, z + (h/2) * d2z)

        d4y = dydt(t + h, y + h * d3y, z + h * d3z)
        d4z = dzdt(t + h, y + h * d3y, z + h * d3z)

        t += h
        y += h/6 * (d1y + 2*d2y + 2*d3y + d4y)
        z += h/6 * (d1z + 2*d2z + 2*d3z + d4z)
        print(t, y, z)

    return (t, y, z)


def rk4_soe(t, y, z, h, n=10):
    # Soeiro style (como está no TEXTO)
    print("Soeiro\nt y z")
    print(t, y, z)
    for i in range(10):
        d1y = h * dydt(t, y, z)
        d1z = h * dzdt(t, y, z)

        d2y = h * dydt(t + h/2, y + d1y/2, z + d1z/2)
        d2z = h * dzdt(t + h/2, y + d1y/2, z + d1z/2)

        d3y = h * dydt(t + h/2, y + d2y/2, z + d2z/2)
        d3z = h * dzdt(t + h/2, y + d2y/2, z + d2z/2)

        d4y = h * dydt(t + h, y + d3y, z + d3z)
        d4z = h * dzdt(t + h, y + d3y, z + d3z)

        t += h
        y += d1y/6 + d2y/3 + d3y/3 + d4y/6
        z += d1z/6 + d2z/3 + d3z/3 + d4z/6
        print(t, y, z)

    return (t, y, z)


# instantiate init values and call the methods for the defaul iter num
h = 0.25
t = 1
y = 1
z = 0
rk4_vil(t, y, z, h)
rk4_soe(t, y, z, h)
