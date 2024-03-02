#!/usr/bin/python3
""" dynamic programming task """


def makeChange(coins, total):
    """ makeChange function """
    if total <= 0:
        return 0
    sort_coins = sorted(coins)
    used_coins = []
    i = 0
    while i < len(coins) and total >= 0:
        y = len(coins) - 1
        while y >= 0:
            while total >= sort_coins[y]:
                total -= sort_coins[y]
                used_coins.append(sort_coins[y])
            y -= 1
        i += 1

    if total == 0:
        return len(used_coins)
    return -1
