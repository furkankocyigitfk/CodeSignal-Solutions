def chessKnight(cell):
    x = ord(cell[0]) - ord("a")
    y = int(cell[1]) - 1
    count = 0
    arr = [[1, 2],
           [2, 1],
           [2, -1],
           [1, -2],
           [-1, -2],
           [-2, -1],
           [-2, 1],
           [-1, 2]]

    for move in arr:
        if 0 <= move[0] + x < 8 and 0 <= move[1] + y < 8:
            count += 1

    return count
