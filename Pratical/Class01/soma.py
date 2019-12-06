#!/usr/bin/env python3


expo = 300
result = result2 = 1
for i in range(expo, -(expo+1), -1):
    result += 10 ** i
    result2 += 10 ** -i

print(result)
print(result2)

if result != result2:
    print("different")

else:
    print("equal")
