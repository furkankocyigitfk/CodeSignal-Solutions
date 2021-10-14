def matrixElementsSum(matrix):
    s = 0

    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[i])-1, -1, -1):
            if not isZeroAbove(matrix, i, j):
                s += matrix[i][j]

    return s


def isZeroAbove(matrix, x, y):
    for i in range(x):
        if (matrix[i][y] == 0):
            return True
    return False
