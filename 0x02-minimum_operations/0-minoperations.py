#!/usr/bin/python3
""" Minimum Operations """


def check_prime(n, i, y):
    """ function to check prime """
    if n == 1:
        return i

    if n % y == 0:
        n = n / y
        i += y
        y = 2

    if y == n:
        i += y
        n /= y

    return check_prime(n, i, y + 1)


def minOperations(n):
    """ min operations """
    i = 0
    while (n % 2) == 0:
        n = int(n / 2)
        i += 2
    if n == 1:
        return i
    i = check_prime(n, i, 2)
    return i
