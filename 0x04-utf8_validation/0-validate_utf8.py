#!/usr/bin/python3
""" validate utf-8 """


def check_subsequences(i, data, sequence):
    """ checks subsequence """
    y = i + 1
    valid = True
    if y >= len(data):
        return False
    while y < sequence:
        x = bin(data[y])[2:].zfill(8)
        print(x)
        if not x.startswith('10'):
            valid = False
            break
        y += 1
    return valid


def validUTF8(data):
    """ validate utf based on the leading characters"""
    valid_list = []
    i = 0
    while i < len(data):
        x = bin(data[i])[2:].zfill(8)
        print(x)
        if data[i] < 128 and x.startswith('0'):
            valid_list.append(True)
            i += 1
            continue

        elif x.startswith('110'):
            valid = check_subsequences(i, data, 2)
            valid_list.append(valid)
            i += 2
            continue
        elif x.startswith('1110'):
            valid = check_subsequences(i, data, 3)
            valid_list.append(valid)
            i += 3
            continue
        elif x.startswith('11110'):
            valid = check_subsequences(i, data, 4)
            valid_list.append(valid)
            i += 4
            continue
        return False
        i += 1

    if False in valid_list:
        return False
    return True
