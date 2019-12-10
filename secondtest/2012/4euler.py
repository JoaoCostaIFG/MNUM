#!/usr/bin/env pytho3

# CHECKED


def dvdu(u, v):
    return (u * (u/2 + 1) * (v**3)) + ((u + 5/2) * (v**2))


u = 1
v = 0.1
h = 0.08

print("s:\n", u, v)
while (u <= 1.8):
    v += dvdu(u, v) * h
    u += h
s = v
print(u, s)


u = 1
v = 0.1
h = 0.08/2

print("sl:\n", u, v)
while (u <= 1.8):
    v += dvdu(u, v) * h
    u += h
sl = v
print(u, sl)


u = 1
v = 0.1
h = 0.08/4

print("sll:\n", u, v)
while (u <= 1.8):
    v += dvdu(u, v) * h
    u += h
sll = v
print(u, sll)

qc = (sl - s) / (sll - sl)
print("QC:", qc)

# metodo ordem 1
# (sll - sl) / (2^ordem - 1)
erro = (sll - sl) / 1
print("Erro:", erro)
