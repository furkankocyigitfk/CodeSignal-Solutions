def minesweeper(matrix):
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    outMatrix = [None] * len(matrix)
    for i in range(len(matrix)):
        outMatrix[i] = [0] * len(matrix[i])
        for j in range(len(matrix[i])):
            if i != top:
                outMatrix[i][j] += matrix[i - 1][j]
            if i != bottom:
                outMatrix[i][j] += matrix[i + 1][j]
            if j != left:
                outMatrix[i][j] += matrix[i][j - 1]
            if j != right:
                outMatrix[i][j] += matrix[i][j + 1]
            if i != top and j != left:
                outMatrix[i][j] += matrix[i - 1][j - 1]
            if i != top and j != right:
                outMatrix[i][j] += matrix[i - 1][j + 1]
            if i != bottom and j != left:
                outMatrix[i][j] += matrix[i + 1][j - 1]
            if i != bottom and j != right:
                outMatrix[i][j] += matrix[i + 1][j + 1]
    return outMatrix
