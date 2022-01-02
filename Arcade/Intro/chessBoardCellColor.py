def chessBoardCellColor(cell1, cell2):
    return getColor(cell1) == getColor(cell2)


def getColor(cell):
    if((ord(cell[0]) - ord("A") + 1) + int(cell[1])) % 2 == 0:
        return "BLACK"
    return "WHITE"
