#!/usr/bin/python3
""" find key fot boxes """


def checkKey(boxes, y, checker):
    """
        recursive function
        -- all boxes get checked except
        the box needs to be unlocked
        -- index of each box checked get sent
        through recursion to avoid that box checked
        in the loop
        Args:
            boxes: array containg all boxes
            y: index for box that needs to be unlocked
            boxState: list create to hold if key is found
    """
    if checker is False and y > 1:
        return checker

    for i in range(len(boxes)):
        checker = False
        if i == y:
            continue
        for value in boxes[i]:
            if value == y:
                checker = True
                break
        if checker is True:
            break
    if y + 1 == len(boxes):
        return checker
    else:
        return checkKey(boxes, y + 1, checker)


def canUnlockAll(boxes):
    """ function to find key for a box """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True
    check = checkKey(boxes, 0, True)
    return check
