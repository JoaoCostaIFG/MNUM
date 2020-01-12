#!/usr/bin/env python3

#  1)
#  Solved in maxima
#  f1: 1/2 * sqrt(exp(x));
#  f2: -1/2 * sqrt(exp(x));
#  f3: exp(x) / (4 * x);

#  plot2d(diff(f1, x), [x, -1, 5], [y, -1, 1]);
#  Converges for X1 and X2

#  plot2d(diff(f2, x), [x, -1, 5], [y, -1, 1]);
#  Converges for X1 and X2

#  plot2d(diff(f3, x), [x, -1, 5], [y, -1, 1]);
#  Converges for X2

#  2)

from math import log


def recorr(x):
    return 2 * log(2 * x)


x0 = 0.9
print(x0)
x1 = recorr(x0)
print(x1)
print("residuo:", x1 - x0)
