#!/usr/bin/env python3

# Read
num = int(input("Number to find the sqrt of? "))

step = input("Step for precision? (default = 0.01) ")
if step == "":
    step = 0.01
else:
    step = float(step)

# Find the nearest perfect square that's smaller than 'num'
index = 0
while index * index < num:
    index += 1
index -= 1

while index * index < num:
    index += step

print("Result: [", index - step, ", ", index, "] with percision of +/-", step/2)

