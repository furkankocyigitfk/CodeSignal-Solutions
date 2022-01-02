def bishopAndPawn(bishop, pawn):
    xdiff = abs(ord(bishop[0]) - ord(pawn[0]))
    ydiff = abs(ord(bishop[1]) - ord(pawn[1]))
    ysum = ord(bishop[1]) + ord(pawn[1])

    if xdiff == ydiff or xdiff == ysum:
        return True
    return False
