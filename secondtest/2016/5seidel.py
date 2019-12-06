#!/usr/bin/env python3

# Checked

A = [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2],
     [-1, 0.25, 4, 2], [2, 4, 1, 8]]
b = [25, 10, 7, -12]
x0 = [2.83865, 2.22131, 4.17630, -3.84236]

x_new = [0, 0, 0, 0]
for i in range(4):
    x_new[i] = b[i]
    for j in range(i):
        x_new[i] -= A[i][j] * x_new[j]

    for j in range(i + 1, 4):
        x_new[i] -= A[i][j] * x0[j]

    x_new[i] /= A[i][i]

print(x_new)
