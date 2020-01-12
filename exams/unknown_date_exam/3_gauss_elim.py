#!/usr/bin/env python3

n = 4
A = [[0.1, 0.5, 3, 0.25], [1.2, 0.2, 0.25, 0.2], [-1, 0.25, 0.3, 2],
     [2, 0.00001, 1, 0.4]]
b = [0, 1, 2, 3]

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

print("A:", A)
print("b:", b)

x = b.copy()
for k in range(n - 1, -1, -1):
    s = 0
    for j in range(k + 1, n):
        s = s + A[k][j] * x[j]

    x[k] = (b[k] - s) / A[k][k]
print("x:", x)

# External stability
print("External stability")
A = [[0.1, 0.5, 3, 0.25], [1.2, 0.2, 0.25, 0.2], [-1, 0.25, 0.3, 2],
     [2, 0.00001, 1, 0.4]]
db = 0.5
da = 0.5
dA = [[da for j in range(n)] for i in range(n)]
b = [db for i in range(n)]

for i in range(n):
    for j in range(n):
        b[i] -= dA[i][j] * x[j]
print("new b:", b)

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

print("A:", A)
print("b:", b)

x = b.copy()
for k in range(n - 1, -1, -1):
    s = 0
    for j in range(k + 1, n):
        s = s + A[k][j] * x[j]

    x[k] = (b[k] - s) / A[k][k]
print("dx:", x)
