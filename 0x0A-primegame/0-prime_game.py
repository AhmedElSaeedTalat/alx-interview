#!/usr/bin/python3
""" module to solve is winner problem """


def checkPrime(n):
    """ check if number is prime """
    i = 2
    while i < n:
        if n % i == 0 and n != i:
            return False
        i += 1
    return True


def removePrimes(list_number):
    """ remove primes and its multiples """
    player = 'Maria'
    heighest_number = list_number[-1]
    for index, i in enumerate(list_number):
        foundPrime = False
        if index + 1 == len(list_number) and i == 0:
            break
        if i == 1 or i == 0 and index + 1 != len(list_number):
            continue
        if checkPrime(i):
            foundPrime = True
            value = i
            while value <= heighest_number:
                list_number[value - 1] = 0
                value *= i
        if foundPrime:
            if player == 'Maria':
                player = 'Ben'
            else:
                player = 'Maria'
    if player == 'Maria':
        return 'Ben'
    else:
        return 'Maria'


def isWinner(x, nums):
    """ is winner """
    list_number = []
    winners = {'Maria': 0, 'Ben': 0}
    for i in range(x):
        if nums[i] == 1:
            winners['Ben'] += 1
            continue
        if nums[i] == 2:
            winners['Maria'] += 1
            continue
        if nums[i] > 2:
            if len(list_number) > nums[i]:
                shorter_list = list_number[0:nums[i]]
                print(shorter_list)
                winner = removePrimes(shorter_list)
                winners[winner] += 1
            else:
                if i == 0 or not list_number:
                    y = 1
                else:
                    y = list_number[-1] + 1
                while y <= nums[i]:
                    list_number.append(y)
                    y += 1
                winner = removePrimes(list_number)
                winners[winner] += 1
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return 'Ben'
