#!/usr/bin/python3
""" dynamic programming task """


def makeChange(coins, total):
    """ makeChange function """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins)
    processed_list = []
    i = 0
    while i < len(coins):
        j = 0
        row = []
        while j <= total:
            if j == 0:
                value = 0
                row.append(value)
                processed_list.append(row)
                row = []
            else:
                if i == 0:
                    if sorted_coins[i] > j:
                        value = 0
                    else:
                        if j % sorted_coins[i] == 0:
                            value = int(j / sorted_coins[i])
                        else:
                            value = 0
                    processed_list[i].append(value)
                else:
                    if sorted_coins[i] > j:
                        value = processed_list[i - 1][j]
                        processed_list[i].append(value)
                    else:
                        index = j - sorted_coins[i]
                        prev_value = processed_list[i - 1][j]
                        value = min(prev_value, 1 + processed_list[i][index])
                        processed_list[i].append(value)
            j += 1
        i += 1
    min_coins = processed_list[-1][-1]
    if min_coins == 0:
        return -1
    else:
        return min_coins
