#!/usr/bin/python3
""" find key fot boxes """


def checkKey(boxes, y, boxState):
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
    if len(boxState) == len(boxes):
        return boxState

    status = 0
    for i in range(len(boxes)):
        if i == y:
            continue
        for value in boxes[i]:
            if value == y:
                boxState.append(True)
                status = 1
                break
        if status == 1:
            break
    if status == 0:
        boxState.append(False)

    checkKey(boxes, y + 1, boxState)
    return boxState


def canUnlockAll(boxes):
    """ function to find key for a box """
    boxState = checkKey(boxes, 0, [])
    boxState[0] = True
    if False in boxState:
        return False
    return True
