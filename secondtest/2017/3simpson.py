#!/usr/bin/env python3

# CHECKED
# NOTE I suggest this tecnic to working on exercises where we only have a
# table of values (instead of a function). Just rewrite the list for each step,
# keeping only the values you need for that step.

ft2 = [1.04, 0.37, 0.38, 1.49, 1.08, 0.13, 0.64, 0.84, 0.12]
ft1 = [1.04, 0.38, 1.08, 0.64, 0.12]
ft = [1.04, 1.08, 0.12]

a = 0
b = 2
n = 0.25
simp = ft2[0] + ft2[-1]
for i in range(1, len(ft2), 2):
    simp += ft2[i] * 4
for i in range(2, len(ft2) - 1, 2):
    simp += ft2[i] * 2
sll = simp * (n/3)
print(sll)

a = 0
b = 2
n = 0.5
simp = ft1[0] + ft1[-1]
for i in range(1, len(ft1), 2):
    simp += ft1[i] * 4
for i in range(2, len(ft1) - 1, 2):
    simp += ft1[i] * 2
sl = simp * (n/3)
print(sl)

a = 0
b = 2
n = 1
simp = ft[0] + ft[-1]
for i in range(1, len(ft), 2):
    simp += ft[i] * 4
for i in range(2, len(ft) - 1, 2):
    simp += ft[i] * 2
s = simp * (n/3)
print(s)


print((sll - sl) / 15)
