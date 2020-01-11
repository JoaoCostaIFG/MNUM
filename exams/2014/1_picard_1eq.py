#!/usr/bin/env python3

# a)
# Solved in maxima
# f: x^4 - 4 * x ^ 3 + x -1;
# solve(f=0);
# There are 2 real solutions

# b)
# [0, +inf] - yes
# [-0.2, 4] - yes
# [1, 3.5] - no
# [3.5, 4.5] - yes

# c)
# Solved in maxima
# f1: (4 * x^2 - 1/(x^2) + 1/(x^3)) ^ (1/3);
# plot2d(diff(f1, x), [x, -0.2, 10], [y, -1, 1]);
# Converges
#
# f2: 4 - 1/(x^2) + 1/(x^3);
# plot2d(diff(f2, x), [x, -0.2, 10], [y, -1, 1]);
# Converges
#
# f3: -(x^4) + 4 * x^3 + 1;
# plot2d(diff(f3, x), [x, -0.2, 10], [y, -1, 1]);
# Doesn't converge (no interval reaches the root)


def recorr(x):
    return (4 * x**3 - x + 1)**(1 / 4)


x = 4
print(x)
for i in range(2):
    x = recorr(x)
    print(x)
