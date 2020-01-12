#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p3.py

A = [[6, 0.5, 3, 0.25], [1.2, 3, 0.25, 0.2], [-1, 0.25, 4, 2], [2, 4, 1, 8]]
b = [2.5, 3.8, 10, 7]
n = 4
x0 = [-0.81959, 1.40167, 2.15095, 0.11019]  # first solution


# calculate new solution using Gauss-Seidel method
x = [0, 0, 0, 0]

for i in range(n):
    x[i] = b[i]
    for j in range(i):
        x[i] -= (A[i][j] * x[j])
    
    for j in range(i+1, n):
        x[i] -= (A[i][j] * x0[j])
        
print("Answer:", x)