#!/usr/bin/env python3

# CHECKED
# simpson para integrais com apenas 1 step intermedio podem ser simplificados para:
# s = h/3 * (y0 + 4*y1 + y2)

y0 = [1.1, 1.4, 2.6]
y1 = [2.1, 4.9, 2.2]
y2 = [6.3, 1.5, 1.2]
f = [y0, y1, y2]

# calculate 3 single integrals (keeping x constant for each one)
h = 0.9
s = [0, 0, 0]
for x in range(3):
    s[x] = h / 3 * (f[x][0] + 4 * f[x][1] + f[x][2])

print("Single integrals:", s)

# double integral
result = h / 3 * (s[0] + 4 * s[1] + s[2])
print("Double integral:", result)
