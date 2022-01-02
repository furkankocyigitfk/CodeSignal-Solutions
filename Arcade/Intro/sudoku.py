def sudoku(grid):
    for i in range(9):
        visited = [0] * 9
        for j in range(9):
            if visited[grid[i][j] - 1] == 1:
                return False
            else:
                visited[grid[i][j] - 1] = 1

        if 0 in visited:
            return False

    for i in range(9):
        visited = [0] * 9
        for j in range(9):
            if visited[grid[j][i] - 1] == 1:
                return False
            else:
                visited[grid[j][i] - 1] = 1
        if 0 in visited:
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            visited = [0] * 9
            for k in range(3):
                for l in range(3):
                    if visited[grid[i+k][j+l] - 1] == 1:
                        return False
                    else:
                        visited[grid[i+k][j+l] - 1] = 1
            if 0 in visited:
                return False

    return True
