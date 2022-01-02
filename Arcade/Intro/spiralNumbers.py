def spiralNumbers(n):
    matrix = [[0] * n for i in range(n)]
    move = [[0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]]

    x = 0
    y = -1
    k = 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += move[i % 4][0]
            y += move[i % 4][1]
            matrix[x][y] = k
            k += 1

    return matrix
