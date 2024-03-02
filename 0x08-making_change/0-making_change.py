#!/usr/bin/python3
""" dynamic programming task """


def makeChange(coins, total):
    """ makeChange function """
    if total <= 0:
        return 0
    sort_coins = sorted(coins)
    used_coins = []
    i = len(coins) - 1
    while i > 0:
        while total >= sort_coins[i]:
            total -= sort_coins[i]
            used_coins.append(sort_coins[i])
        i -= 1
    if total == 0:
        return len(used_coins)
    return -1
