#!/usr/bin/python3
""" module to create pascal's triangle """


def pascal_triangle(n):
    """ pascal traingle """
    if n <= 0:
        return []
    main_list = []
    main_list.append([1])
    nested_list = []
    i = 1
    while i < n:
        nested_list.append(1)
        prev_row = main_list[i - 1]
        if i > 1:
            for y in range(i - 1):
                val = prev_row[y] + prev_row[y + 1]
                nested_list.append(val)
        nested_list.append(1)
        main_list.append(nested_list)
        nested_list = []
        i += 1
    return main_list
