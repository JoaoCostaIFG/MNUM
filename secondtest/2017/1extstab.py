#!/usr/bin/env python3

# CHECKED
# NOTE IMO this exercise sucks. I just translated what the teached did in MAXIMA to python
# in one of the examples in the "TEXT"
# In this case:
# [ dB ]   [ dA, dA, dA ]   [ X01 ]
# [ dB ] - [ dA, dA, dA ] * [ X02 ] = new_b
# [ dB ]   [ dA, dA, dA ]   [ X03 ]
# and we just solve the original matrix, A, for this new b array, b

A = [[18, -1, 1], [3, -5, 4], [6, 8, 29]]
b = [10, 2, -1]
x0 = [0.552949, -0.15347, -0.10655]
b = [0.1 - 0.1 * (x0[0] + x0[1] + x0[2]), 0.1 - 0.1 * (x0[0] + x0[1] + x0[2]), 0.1 - 0.1 * (x0[0] + x0[1] + x0[2])]

for i in range(3):
    oldA = A[i][i]
    b[i] /= oldA
    for j in range(3):
        A[i][j] /= oldA

    for j in range(i + 1, 3):
        nextA = A[j][i]
        b[j] -= b[i] * nextA
        for k in range(3):
            A[j][k] -= A[i][k] * nextA


x = [0, 0, 0]
x[2] = b[2] / A[2][2]
x[1] = (b[1] - x[2] * A[1][2]) / A[1][1]
x[0] = (b[0] - x[1] * A[0][1] - x[2] * A[0][2]) / A[0][0]

print(x)
