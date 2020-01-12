#!/usr/bin/env python3

n = 3
A = [[18, -1, 1], [3, -5, 4], [6, 8, 29]]
x = [0.552949, -0.15347, -0.10655]

db = da = 0.1
b = [db for i in range(n)]
dA = [[da for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        b[i] -= dA[i][j] * x[j]

print("new b:", b)

# Gauss elim

for i in range(n):
    pivot = A[i][i]
    b[i] /= pivot
    for j in range(n):
        A[i][j] /= pivot

    for j in range(i + 1, n):
        times = A[j][i]
        b[j] -= times * b[i]
        for k in range(n):
            A[j][k] -= times * A[i][k]

print(A)
print(b)

# Get x (external stability)
x = b.copy()
for k in range(n - 1, -1, -1):
    s = 0
    for j in range(k + 1, n):
        s += A[k][j] * x[j]

    x[k] = (b[k] - s) / A[k][k]

print("extern stab:", x)
