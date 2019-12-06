#!/usr/bin/env python3

# Pesquisa binaria
# Read
num = int(input("Number to find the sqrt of? "))

index = 0
step = num / 2
prox = True

while abs(index * index - num) > 1e-10:
    if (prox):
        index += step
    else:
        index -= step
    step = step / 2

    if (index * index) < num:
        prox = True
    else:
        prox = False

print("Result: [", index - 2 * step, ", ", index, "] with percision of +/-", step)

