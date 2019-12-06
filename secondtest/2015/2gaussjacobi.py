#!/usr/bin/env python3

# CHECKED

A = [[4.5, -1, -1, 1], [-1, 4.5, 1, -1], [-1, 2, 4.5, -1], [2, -1, -1, 4.5]]
b = [1, -1, -1, 0]
x = [0.25, 0.25, 0.25, 0.25]
new_x = [0, 0, 0, 0]


for k in range(2):
    for i in range(4):
        new_x[i] = b[i]
        for j in range(4):
            if i != j:
                new_x[i] -= A[i][j] * x[j]

        new_x[i] *= (1 / A[i][i])
    print(new_x)
    x = new_x



# GAUSS NORMAL
#  for i in range(4):
    #  pric = A[i][i]
    #  b[i] /= pric
    #  for j in range(4):
        #  A[i][j] /= pric

    #  for j in range(i + 1, 4):
        #  times = A[j][i]
        #  b[j] -= times * b[i]
        #  for k in range(4):
            #  A[j][k] -= times * A[i][k]

