#!/usr/bin/env python3


def dydt(t, y, k):
    return (-k * t - y) / 20

ans = 0.5 # after 11 steps, we should get y ~= 0.5

# k = 5
h = 0.2
t = 0
y = 0
k = 5
for i in range(11):
    y += h * dydt(t, y, k)
    t += h
    print(t, y)
print("diff for k = 5:", abs(ans - y))

# k = 20
h = 0.2
t = 0
y = 0
k = 20
for i in range(11):
    y += h * dydt(t, y, k)
    t += h
    print(t, y)
print("diff for k = 20:", abs(ans - y))

# k = 40
h = 0.2
t = 0
y = 0
k = 40
for i in range(11):
    y += h * dydt(t, y, k)
    t += h
    print(t, y)
print("diff for k = 40:", abs(ans - y))
