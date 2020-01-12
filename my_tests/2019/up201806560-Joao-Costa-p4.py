#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# up201806560-Joao-Costa-p4.py

def dvdu(u, v):
    return u * (u/2 + 1) * (v**3) + (u + 2.5) * (v**2)

# s
u = 1
v = 0.15
uf = 2
h = 0.1
while (u < uf):
    v += dvdu(u, v) * h
    u += h

s = v
print("h:", h, "u:", u, "v:", v)

# sl
u = 1
v = 0.15
uf = 2
h = 0.1/2
while (u < uf):
    v += dvdu(u, v) * h
    u += h

sl = v
print("h:", h, "u:", u, "v:", v)

# sll
u = 1
v = 0.15
uf = 2
h = 0.1/4
while (u < uf):
    v += dvdu(u, v) * h
    u += h

sll = v
print("h:", h, "u:", u, "v:", v)

# QC
QC = (sl - s) / (sll - sl)
print("QC:", QC)

# Erro
order_euler = 1
err = (sll - sl) / (2 ** order_euler - 1)
print("Erro:", err)