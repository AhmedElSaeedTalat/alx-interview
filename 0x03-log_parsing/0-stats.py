#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
from sys import stdin
import re


pattern = r'^[\d+\.]+ - \[[\d+-: ]+\] \S+ \/\S+ \S+ (\d+) (\d+)$'
total_size: int = 0
count: int = 0
status_dic: dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                    405: 0, 500: 0}
try:
    for line in stdin:
        match = re.match(pattern, line)
        if match:
            status, size = match.groups()
            try:
                total_size += int(size)
                status_dic[int(status)] += 1
            except Exception:
                pass
            count += 1
        else:
            continue

        if count == 10:
            print('File size:', total_size)
            for key, value in status_dic.items():
                if value > 0:
                    print(f'{key}: {value}')
            count = 0
except KeyboardInterrupt:
    print('File size:', total_size)
    for key, value in status_dic.items():
        if value > 0:
            print(f'{key}: {value}')
        count = 0
