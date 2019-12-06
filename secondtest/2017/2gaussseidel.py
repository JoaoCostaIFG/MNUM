#!/usr/bin/env python3

# CHECKED

A = [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]]
b = [25, 10, 7, -12]
x0 = [2.12687, 2.39858, 3.99517, -3.73040]

xnew = [0, 0, 0, 0]
for i in range(4):
    xnew[i] = b[i]

    for j in range(i):
        xnew[i] -= (A[i][j] * xnew[j])

    for j in range(i + 1, 4):
        xnew[i] -= (A[i][j] * x0[j])

    xnew[i] /= A[i][i]

print(xnew)
