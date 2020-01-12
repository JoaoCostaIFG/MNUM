#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p1.py

# integral pelo metodo de Simpson
# s = h/3 * (y0 + 4*y1 + y2)

# Wt e a funcao tabelada
Wt = [0.0000000000, 0.0073522983, 0.1806367724,
      0.9465361603, 3.0161883586, 7.3851864223,
      15.3335785653, 28.4258681599, 48.5110137371,
      77.7224289867, 118.4779827567, 173.4799990541,
      245.7152570443, 338.4549910514, 455.2548905581,
      599.9551002058, 776.6802197943]


# calculo do integral pela regra de Simpson (step = 1)
h = 1  # step
n = 16 # table size
simp = Wt[0] + Wt[-1]

temp_sum = 0
for i in range(1, n, 2):
    temp_sum += Wt[i]
simp += temp_sum * 4

temp_sum = 0
for i in range(2, n-1, 2):
    temp_sum += Wt[i]
simp += temp_sum * 2

simp *= (h/3)
print("O valor do integral definido e:", simp, "\nstep:", h)
sll = simp


# calculo do integral pela regra de Simpson (step = 1/2)
Wt2 = [0.0000000000, 0.1806367724,
       3.0161883586, 15.3335785653,
       48.5110137371, 118.4779827567,
      245.7152570443, 455.2548905581,
      776.6802197943]

h = 1 * 2 # step
n = 8 # table size
simp = Wt2[0] + Wt2[-1]

temp_sum = 0
for i in range(1, n, 2):
    temp_sum += Wt2[i]
simp += temp_sum * 4

temp_sum = 0
for i in range(2, n-1, 2):
    temp_sum += Wt2[i]
simp += temp_sum * 2

simp *= (h/3)
print("O valor do integral definido e:", simp, "\nstep:", h)
sl = simp


# calculo do integral pela regra de Simpson (step = 1/2)
Wt3 = [0.0000000000,
       3.0161883586,
       48.5110137371,
      245.7152570443,
      776.6802197943]

h = 1 * 4 # step
n = 4 # table size
simp = Wt3[0] + Wt3[-1]

temp_sum = 0
for i in range(1, n, 2):
    temp_sum += Wt3[i]
simp += temp_sum * 4

temp_sum = 0
for i in range(2, n-1, 2):
    temp_sum += Wt3[i]
simp += temp_sum * 2

simp *= (h/3)
print("O valor do integral definido e:", simp, "\nstep:", h)
s = simp


# calculo do QC
QC = (sl - s) / (sll - sl)
print("QC:", QC)

# calculo do erro
simp_order = 4
err = (sll - sl) / (2**simp_order - 1)
print("Erro absoluto:", err)