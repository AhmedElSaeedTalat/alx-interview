#!/usr/bin/python3
""" rotate 2d in place """


def swap(matrix, i, j):
    """ swap function """
    temp = matrix[i][j]
    matrix[i][j] = matrix[j][i]
    matrix[j][i] = temp


def rotate_2d_matrix(matrix):
    """ rotate 2d """
    i = 0
    while i <= len(matrix) - 2:
        j = i + 1
        while j <= len(matrix) - 1:
            swap(matrix, i, j)
            j += 1
        i += 1

    i = 0
    while i < len(matrix):
        matrix[i].reverse()
        i += 1
