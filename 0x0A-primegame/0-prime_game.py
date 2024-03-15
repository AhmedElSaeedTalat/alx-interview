#!/usr/bin/python3
""" module to solve is winner problem """


def checkPrime(n, primes):
    """ check if number is prime """
    if n in primes:
        return primes[n]
    i = 2
    while i < n:
        if n % i == 0 and n != i:
            primes[n] = False
            return False
        i += 1
    primes[n] = True
    return True


def removePrimes(list_number, primes):
    """ remove primes and its multiples """
    player = 'Maria'
    foundPrime = False
    for index, i in enumerate(list_number):
        if foundPrime is True:
            if player == 'Maria':
                player = 'Ben'
            else:
                player = 'Maria'
        foundPrime = False
        if index + 1 == len(list_number) and i == 0:
            break
        if i == 1 or i == 0 and index + 1 != len(list_number):
            continue
        if checkPrime(i, primes):
            foundPrime = True
            list_number[index] = 0
            value = i
            if index + 1 < len(list_number):
                y = index + 1
                while y < len(list_number):
                    if list_number[y] % value == 0:
                        list_number[y] = 0
                    y += 1
    list_number = []
    if foundPrime and player:
        return {'winnerName': player, 'primes': primes}
    else:
        if player == 'Maria':
            return {'winnerName': 'Ben', 'primes': primes}
        else:
            return {'winnerName': 'Maria', 'primes': primes}


def isWinner(x, nums):
    """ is winner """
    list_number = []
    primes = {}
    if not nums or max(nums) == 1:
        return None
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
                winner = removePrimes(shorter_list, primes)
                winners[winner['winnerName']] += 1
            else:
                if i == 0 or not list_number:
                    y = 1
                else:
                    y = list_number[-1] + 1
                while y <= nums[i]:
                    list_number.append(y)
                    y += 1
                winner = removePrimes(list(list_number), primes)
                winners[winner['winnerName']] += 1
                primes = winner['primes']
    if winners['Maria'] == winners['Ben']:
        return None
    if winners['Maria'] > winners['Ben']:
        return 'Maria'
    else:
        return 'Ben'
