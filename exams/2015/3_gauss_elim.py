#!/usr/bin/env python3

# Get superior triangular matrix a)
n = 3
A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
b = [-1, 1, 1]

for i in range(n):
    pivot = A[i][i]
    b[i] /= pivot
    for j in range(n):
        A[i][j] /= pivot

    for j in range(i+1, n):
        times = A[j][i]
        b[j] -= times * b[i]
        for k in range(n):
            A[j][k] -= times * A[i][k]

print("A:", A)
print("b:", b)


# Get x  b)
x = [0, 0, 0]
x[2] = b[2]
x[1] = b[1] - A[1][2] * x[2]
x[0] = b[0] - A[0][2] * x[2] - A[0][1] * x[1]
print("x:", x)


# EXTERNAL STABILITY
# A.dx = db - dA.x
# don't feel like importing copy
A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
# calculate new b
dA = 0.05
db = 0.05
nA = [[dA, dA, dA], [dA, dA, dA], [dA, dA, dA]]
b = [db, db, db]
for i in range(n):
    for j in range(n):
        b[i] -= nA[i][j] * x[j]

# solve new system
for i in range(n):
    pivot = A[i][i]
    b[i] /= pivot
    for j in range(n):
        A[i][j] /= pivot

    for j in range(i+1, n):
        times = A[j][i]
        b[j] -= times * b[i]
        for k in range(n):
            A[j][k] -= times * A[i][k]

print("\nA:", A)
print("b:", b)

# Get x (external stability)
x = [0, 0, 0]
x[2] = b[2]
x[1] = b[1] - A[1][2] * x[2]
x[0] = b[0] - A[0][2] * x[2] - A[0][1] * x[1]
print("stablity:", x)


# The one with the most sensitivity to erros is x3 (aka x[2] or z) d)
# abs(x[0] < x[1] < x[2])
print("most sensitive:", max(abs(i) for i in x))
