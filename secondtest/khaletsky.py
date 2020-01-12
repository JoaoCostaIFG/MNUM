#!/usr/bin/env python3

# CHECKED

A = [[4.8, 1, 1, 1], [1, 4.8, 1, 1], [1, 1, 4.8, 1], [1, 1, 1, 4.8]]
b = [1, -1, -1, 0]
n = 4

B = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
C = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
for i in range(n):
    B[i][0] = A[i][0]

for i in range(n):
    C[0][i] = A[0][i] / B[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j):
            B[i][j] = A[i][j]
            for k in range(j):
                B[i][j] -= (B[i][k] * C[k][j])
        else:
            C[i][j] = A[i][j]
            for k in range(i):
                C[i][j] -= (B[i][k] * C[k][j])
            C[i][j] /= B[i][i]

print(*B, sep='\n')
print()
print(*C, sep='\n')

# getting y
# B.y = b
y = b.copy()
for i in range(n):
    s = 0
    for j in range(i-1, -1, -1):
        s += B[i][j] * y[j]

    y[i] = (b[i] - s) / B[i][i]

# C.x = y
x = y.copy()
for i in range(n-1, -1, -1):
    s = 0
    for j in range(i+1, n):
        s += C[i][j] * x[j]

    x[i] = (y[i] - s) / C[i][i]

print(x)
print()
print(y)
