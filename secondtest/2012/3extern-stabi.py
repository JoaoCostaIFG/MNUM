#!/usr/bin/env python3

# CHECKED
# pretty much the same shit as gauss but we need to solve for a different b
# new_b = dB - dA * X

n = 3  # order of the matrix
A = [[0.7, 8, 3], [-6, 0.45, -0.25], [8, -3.1, 1.05]]
b = [12, 15, 23]

# using da as the error for all data
da = db = 0.5
# matrix of errors for each value in the matrix A
dA = [[da, da, da], [da, da, da], [da, da, da]]
# array of errors for each value in the array b
dB = [db, db, db]

# get the new_b (if the values are all the same, just hard code it)
x0 = [-4.3716, -8.9325, 28.8401]  # the values we got for the result using gauss elimination
# line below if the hard-coded version
#  b = [0.5 - 0.5 * (x0[0] + x0[1] + x0[2]), 0.5 - 0.5 * (x0[0] + x0[1] + x0[2]), 0.5 - 0.5 * (x0[0] + x0[1] + x0[2])]
new_b = []
for i in range(3):
    new_b.append(0)
    temp_val = 0
    for j in range(3):
        temp_val += dA[i][j] * x0[j]
    new_b[i] = dB[i] - temp_val
b = new_b

print("new b:", b)

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
