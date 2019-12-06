#!/usr/bin/env python3

# CHECKED

A = [[4.5, -1, -1, 1], [-1, 4.5, 1, -1], [-1, 2, 4.5, -1], [2, -1, -1, 4.5]]
b = [1, -1, -1, 0]
x = [0.25, 0.25, 0.25, 0.25]
x_new = [0, 0, 0, 0]

for k in range(2):
    for i in range(4):
        x_new[i] = b[i]
        for j in range(4):
            if j != i:
                x_new[i] -= A[i][j] * x[j]

        x_new[i] *= (1 / A[i][i])

    print("Ans", k, "\n", x_new)
    x = x_new.copy()

