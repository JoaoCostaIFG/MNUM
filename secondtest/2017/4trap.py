#!/usr/bin/env python3

# CHECKED
# NOTE I recommend hard-coding the double integral exercises like this
# whenever you are able too because they become really short and easy to write

y0 = [1.1, 1.4, 7.7]
y1 = [2.1, 3.1, 2.2]
y2 = [7.3, 1.5, 1.2]
y = [y0, y1, y2]

h = 1
x = 0
int1 = (h / 2) * (y[0][x] + 2*y[1][x] + y[2][x])
x = 1
int2 = (h / 2) * (y[0][x] + 2*y[1][x] + y[2][x])
x = 2
int3 = (h / 2) * (y[0][x] + 2*y[1][x] + y[2][x])

final = (h / 2) * (int1 + 2*int2 + int3)
print(final)
