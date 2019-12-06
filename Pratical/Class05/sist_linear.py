#!/usr/bin/env python3

mtr = [[7, 3, 1, 24], [11, 13, 3, 64], [3, 11, 17, 56]]
mtr2 = [[7, 3, 1, 24], [11, 13, 3, 64], [3, 11, 17, 56]]


def ptr():
    for item in mtr:
        print(' '.join(str(x) for x in item))


# Gauss
for diag in range(3):
    pivot = mtr[diag][diag]

    for col in range(4):
        mtr[diag][col] /= pivot  # error prof por n guardar var

    for lin in range(diag+1, 3):
        pivot = mtr[lin][diag]
        for col in range(diag, 4):
            mtr[lin][col] = mtr[lin][col] - pivot * mtr[diag][col]
ptr()


# Subst
z = y = x = ""
for i in range(2, -1, -1):
    if (z == ""):
        z = mtr[i][3] / mtr[i][i]
    elif (y == ""):
        y = (mtr[i][3] - z*mtr[i][2]) / mtr[i][i]
    else:
        x = (mtr[i][3] - z*mtr[i][2] - y*mtr[i][1]) / mtr[i][i]
print("\nx:", x, "y:", y, "z:", z)


# Residuos  A.erro=residuo
# erro = [2-x, 3-y, 1-z]
erro = [2-2.05, 3-3.2, 1-0.89]
# residuo = [sum(t) for t in zip(mtr)]
residuo = []
for i in range(3):
    summ = 0
    for j in range(3):
        summ += (mtr2[i][j] * erro[j])
    residuo.append(summ)

print("\nResiduo:", residuo)


# Distribuicao do residuo


















# 1st pivot
# pivot = mtr[0][0]
# for i in range(4):
    # mtr[0][i] = mtr[0][i] / pivot

# 2nd line zerar
# pivot = mtr[1][0]
# for i in range(4):
    # mtr[1][i] = mtr[1][i] - pivot * mtr[0][i]

# 3rd line zerar
# pivot = mtr[2][0]
# for i in range(4):
    # mtr[2][i] = mtr[2][i] - pivot * mtr[0][i]


# 2nd pivot
# pivot = mtr[1][1]
# for i in range(1, 4):
    # mtr[1][i] = mtr[1][i] / pivot

# 1st line zerar
# pivot = mtr[0][1]
# for i in range(1, 4):
    # mtr[0][i] = mtr[0][i]
