#!/usr/bin/env python3

# CHECKED

n = 3  # order of the matrix
A = [[0.7, 8, 3], [-6, 0.45, -0.25], [8, -3.1, 1.05]]
b = [12, 15, 23]

# diagonalizar matriz
for i in range(n):
    diag_val = A[i][i]

    b[i] /= diag_val
    for j in range(n):
        A[i][j] /= diag_val

    for j in range(i + 1, n):
        times = A[j][i]

        b[j] -= b[i] * times
        for k in range(n):
            A[j][k] -= A[i][k] * times

print("Matrix:", A)

# solve for x, y, z
# using copy because we are going to change this array and need the old info
ans = b.copy()
for i in range(n - 1, -1, -1):
    s = 0
    for j in range(i + 1, n):
        s += A[i][j] * ans[j]

    ans[i] = (b[i] - s) / A[i][i]

print("Answer:", ans)
