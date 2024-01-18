#!/usr/bin/python3
""" Minimum Operations """
from math import sqrt


def minOperations(n):
    """ min operations """
    i = 0
    while (n % 2) == 0:
        n = int(n / 2)
        i += 2
    if n == 1:
        return i
    num = int(sqrt(n))
    if num == 1:
        i += n
        return i
    if n % num == 0:
        i += num
        y = 2
        while num % y != 0 or y < num:
            y += 1
        i += y
    return i
