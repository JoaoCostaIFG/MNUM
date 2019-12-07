#!/usr/bin/env python3

# Checked
# I solver the version on the '2016.pdf', not the image files
# (same test, different version => different question order and given values)

ft = [1.02, 1.21, 1.45, 0.89, 0.62, 1.46, 0.74, 0.36, 0.87]
ft2 = [1.02, 1.45, 0.62, 0.74, 0.87]
ft3 = [1.02, 0.62, 0.87]
h = 0.2
a = 0
b = 1.6
simp = ft[0] + ft[-1]
temp_s = 0
for i in range(1, 8, 2):
    temp_s += ft[i]
simp += 4 * temp_s
temp_s = 0
for i in range(2, 7, 2):
    temp_s += ft[i]
simp += 2 * temp_s
simp *= (h/3)
sll = simp
print(simp)


h = 0.4
a = 0
b = 1.6
simp = ft2[0] + ft2[-1]
temp_s = 0
for i in range(1, 4, 2):
    temp_s += ft2[i]
simp += 4 * temp_s
temp_s = 0
for i in range(2, 3, 2):
    temp_s += ft2[i]
simp += 2 * temp_s
simp *= (h/3)
sl = simp
print(simp)

err = (sll - sl) / 15
print(err)
