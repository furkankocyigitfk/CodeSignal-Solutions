def sudoku2(grid):
    for i in range(9):
        a = set()
        for j in range(9):
            if grid[i][j] != '.':
                if grid[i][j] not in a:
                    a.add(grid[i][j])
                else:
                    return False

        a = set()
        for j in range(9):
            if grid[j][i] != '.':
                if grid[j][i] not in a:
                    a.add(grid[j][i])
                else:
                    return False

    for i in range(1, 9, 3):
        for j in range(1, 9, 3):
            a = set()
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if grid[k][l] != '.':
                        if grid[k][l] not in a:
                            a.add(grid[k][l])
                        else:
                            return False
    return True
