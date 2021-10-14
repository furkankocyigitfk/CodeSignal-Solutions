def boxBlur(matrix):
    blurred = list()
    for i in range(1, len(matrix) - 1):
        arr = list()
        for j in range(1, len(matrix[i]) - 1):
            arr.append(blurMatrix(matrix, i, j))

        blurred.append(arr)
    return blurred


def blurMatrix(matrix, x, y):
    s = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            s += matrix[i][j]

    return s // 9
