#!/usr/bin/env python3

# CHECKED
# The answers on the pdf were wrong, except for the first value of x1
# (I believe mine are right because I get the same results when using old, correct. code)

# a)
n = 4  # matrix order
A = [[4.9, -1, -1, 1], [-1, 4.8, 1, -1], [-1, 2, 4.8, -1], [2, -1, -1, 4.8]]
b = [1, -1, -1, 0]

x0 = [0, 0, 0, 0]
x = [0, 0, 0, 0]

for k in range(2):
    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            x[i] -= A[i][j] * x[j]

        for j in range(i+1, n):
            x[i] -= A[i][j] * x0[j]

        x[i] /= A[i][i]

    # if doing more than 1 iteration, copy method is very important
    # (see python's soft and hard copies)
    x0 = x.copy()
    print(x)


# b)
# The process converges because the absolute value of each element on the main
# diagonal of the matrix ([4.8, 4.8, 4.8, 4.8]) is greater than or equal to (diagonally dominant)
# the sum of the absolute values of all other elements in their respective lines:
# i=1   4.8 > 3
# i=2   4.8 > 3
# i=3   4.8 > 4
# i=4   4.8 > 4
