#!/usr/bin/env python3

A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
b = [-1, 1, 1]
n = 3

for i in range(n):
    pivot = A[i][i]
    b[i] /= pivot
    for j in range(n):
        A[i][j] /= pivot

    for j in range(i+1, n):
        times = A[j][i]
        b[j] -= b[i] * times

        for k in range(n):
            A[j][k] -= times * A[i][k]

print(A)
print(b)

# solution
x = [0, 0, 0]
x[2] = b[2] / A[2][2]
x[1] = (b[1] - x[2] * A[1][2]) / A[1][1]
x[0] = (b[0] - x[2] * A[0][2] - x[1] * A[0][1]) / A[0][0]
print(x)


# external stability
dA = 0.05
db = 0.05
b = [db for i in range(n)]
dA = [[dA for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        b[i] -= dA[i][j] * x[j]


print("external stabilty")
A = [[1, 1/2, 1/3], [1/2, 1/3, 1/4], [1/3, 1/4, 1/5]]
for i in range(n):
    pivot = A[i][i]
    b[i] /= pivot
    for j in range(n):
        A[i][j] /= pivot

    for j in range(i+1, n):
        times = A[j][i]
        b[j] -= b[i] * times

        for k in range(n):
            A[j][k] -= times * A[i][k]

print(A)
print(b)

# solution
x = [0, 0, 0]
x[2] = b[2] / A[2][2]
x[1] = (b[1] - x[2] * A[1][2]) / A[1][1]
x[0] = (b[0] - x[2] * A[0][2] - x[1] * A[0][1]) / A[0][0]
print(x)

print("most sensible to errors:", max(abs(i) for i in x))
