#!/usr/bin/env python3

import math

# E as a constant
# inicial_deposit = math.e - 1
inicial_deposit = 2.72182

final_capital = inicial_deposit
for i in range(1, 26):
    final_capital *= i
    final_capital -= 1
    #print("Iter", i, "-", final_capital)

print("Final capital (const): {:.4e}".format(final_capital))


# E as a function result
inicial_deposit = math.exp(1) - 1

final_capital = inicial_deposit
for i in range(1, 26):
    final_capital *= i
    final_capital -= 1
    #print("Iter", i, "-", final_capital)

print("Final capital (function): {:.4e}".format(final_capital))

