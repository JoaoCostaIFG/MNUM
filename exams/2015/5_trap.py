from math import sqrt, e

k = 2.5


def f(x):
    return sqrt(1 + (k * e**(k*x))**2)


# S
a = 0
b = 1
h = 0.125
n = int((b - a) / h)
trap = f(a) + f(b)

temp = 0
for i in range(1, n):
    temp += f(a + h * i)
trap += temp * 2
s = h/2 * trap
print("trap s:", s)

# Sl
a = 0
b = 1
h = 0.125/2
n = int((b - a) / h)
trap = f(a) + f(b)

temp = 0
for i in range(1, n):
    temp += f(a + h * i)
trap += temp * 2
sl = h/2 * trap
print("trap sl:", sl)

# Sll
a = 0
b = 1
h = 0.125/4
n = int((b - a) / h)
trap = f(a) + f(b)

temp = 0
for i in range(1, n):
    temp += f(a + h * i)
trap += temp * 2
sll = h/2 * trap
print("trap sll:", sll)


# QC
qc = (sl - s) / (sll - sl)
print("QC:", qc)
# erro
erro = (sll - sl) / (2**2 - 1)
print("erro:", erro)
