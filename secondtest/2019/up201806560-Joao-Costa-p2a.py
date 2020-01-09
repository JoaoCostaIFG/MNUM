#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p2a.py

from math import sqrt

# matrix e vetores iniciais
n = 3
A = [[0.000030, 0.213472, 0.332147], [0.215512, 0.375623, 0.476625], [0.173257, 0.663257, 0.625675]]
b = [0.235262, 0.127653, 0.285321]

solA = [ -0.931614, 0.003901, -0.705882 ]
solB = [ 0.674262, 0.053108, -0.991431 ]

# residuo para solucao A
print("Residuo da solucao A:")
resA = [0, 0, 0]
for i in range(n):
    resA[i] = 0
    for j in range(n):
        resA[i] += A[i][j] * solA[j]
print(resA)
# norma deste residuo
normaresA = 0
for i in range(n):
    normaresA += (resA[i] ** 2)
normaresA = sqrt(normaresA)
print(normaresA)

# residuo para solucao B
print("Residuo da solucao B:")
resB = [0, 0, 0]
for i in range(n):
    resB[i] = 0
    for j in range(n):
        resB[i] += A[i][j] * solB[j]
print(resB)
# norma deste residuo
normaresB = 0
for i in range(n):
    normaresB += (resB[i] ** 2)
normaresB = sqrt(normaresB)
print(normaresB)