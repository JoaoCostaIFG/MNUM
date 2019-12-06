#!/usr/bin/env python3

import math
import copy

mtr = [[7, 3, 1, 24], [11, 13, 3, 64], [3, 11, 17, 56]]
n = len(mtr)
b = [24, 64, 56]
mtr2 = [[7, 3, 1, 24], [11, 13, 3, 64], [3, 11, 17, 56]]


def ptr():
    print("\nmatrix:")
    for item in mtr:
        print(' '.join(str(x) for x in item))
    print()


def gauss():
    # Gauss
    for diag in range(n):
        pivot = mtr[diag][diag]

        for col in range(n+1):
            mtr[diag][col] /= pivot

        for lin in range(diag+1, n):
            pivot = mtr[lin][diag]
            for col in range(diag, n+1):
                mtr[lin][col] = mtr[lin][col] - pivot * mtr[diag][col]
    ptr()


    # Subst
    my_sol = [mtr[0][3], mtr[1][3], mtr[2][3]]
    for i in range(1, -1, -1):
        for j in range(i+1, n):
            my_sol[i] -= mtr[i][j]*my_sol[j]
        my_sol[i] /= mtr[i][i]

    print("Sol:", my_sol)
    return my_sol


def resed(my_sol):
    # Residuos  A.erro=residuo=b - A.x0
    residuo = b.copy()
    for i in range(3):
        summ = 0
        for j in range(3):
            summ += (mtr2[i][j] * my_sol[j])
        residuo[i] -= summ
    print("\nResiduo:", residuo)


def euclid(x):
    summ = 0
    for i in x:
        summ += i
    return math.sqrt(summ)


def new_b_mtr(b, matra):
    for i in range(len(matra)):
        matra[i][3] = b[i]


my_sol = [2.05, 3.2, 0.89]
for i in range(3):
    res = resed(my_sol.copy())  # residuo

    mtr = copy.deepcopy(mtr2)
    new_b_mtr(res, mtr)

    my_sol = gauss()  # delta
    r


    print("\n")
