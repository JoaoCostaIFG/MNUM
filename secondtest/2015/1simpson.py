#!/bin/bin/env python3

# CHECKED
# NOTE I changed my strategy for this kind of exercises (table of values instead of an expression)
# Just use the list directly instead of making an "x to list index function" for each step
# So just ingore the f(x) function below, it is useless


ft = [0.36, 1.19, 1.32, 0.21, 1.15, 1.39, 0.12, 1.22, 0.60]
fstep = 4


def f(x):
    return ft[int(x * fstep)]


a = 0
b = 2

summ = (f(a) + f(b))
dx = 0.25

temp_summ = 0
for i in range(1, 8, 2):
    temp_summ += ft[i]
summ += (4 * temp_summ)

temp_summ = 0
for i in range(2, 7, 2):
    temp_summ += ft[i]
summ += (2 * temp_summ)

summ *= (dx / 3)
print("Simpson result:", summ)
