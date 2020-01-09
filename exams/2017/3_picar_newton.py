#!/usr/bin/env python3

from math import log, e

erro = 0.001


def recorr(x):
    return log(5 + x)


def f(x):
    return e**x - x - 5


def df(x):
    return e**x - 1


def newton(guess):
    print("newton")
    #  while (abs(guess - old_x) > erro):
    #  print(guess)
    for i in range(10):
        guess = guess - (f(guess) / df(guess))
        print(guess)


def picard(guess):
    print("picard")
    #  while (abs(guess - old_x) > erro):
    #  print(guess)
    for i in range(10):
        guess = recorr(guess)
        print(guess)


x0 = 3
newton(x0)
picard(x0)
