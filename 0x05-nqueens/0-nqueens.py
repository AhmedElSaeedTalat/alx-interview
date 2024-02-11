#!/usr/bin/python3
""" Nqueen problem """
import sys


def check_n(args):
    """
        function to chcek n passed as argument
        Args:
            args: passed args to terminal
        Returns - n if no error is detected
    """
    if len(args) != 2:
        print('Usage: nqueens N')
        exit(1)

    n = args[1]
    if not n.isdigit():
        print("N must be a number")
        exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    return n


def queen_recursion(n, chess_board, queen_position, column):
    """ queen recursion """
    if column > 3:
        return queen_position
    for i in range(n):
        if i in queen_position.keys():
            continue
        for y in range(n):
            if i - 1 != -1 and chess_board[i - 1][y] == 'Q':
                continue
            elif i - 1 != -1 and y + 1 != len(chess_board) and \
                    chess_board[i - 1][y + 1] == 'Q':
                continue
            elif i - 1 != -1 and y - 1 != -1 and \
                    chess_board[i - 1][y - 1] == 'Q':
                continue
            if i in queen_position.keys():
                continue
            chess_board[i][y] = 'Q'
            queen_position[i] = y
    positions = []
    for i in chess_board:
        print(i)
    for key, value in queen_position.items():
        positions.append([key, value])
    print(positions)
    queen_position.clear()
    positions.clear()
    if column < 3:
        for i in range(n):
            for y in range(n):
                chess_board[i][y] = 0
        i = y = 0
        chess_board[0][column + 1] = 'Q'
        queen_position[0] = column + 1
        queen_recursion(n, chess_board, queen_position, column + 1)


def check_queen(n: int):
    """ check queens """
    chess_board = []
    for i in range(n):
        chess_board.append([])
        for y in range(n):
            chess_board[i].append(0)
    chess_board[0][0] = 'Q'
    quen_position = {0: 0}
    queen_recursion(n, chess_board, quen_position, 0)


args = sys.argv
n = check_n(args)
check_queen(n)
