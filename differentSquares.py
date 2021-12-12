def differentSquares(matrix):
    s = set()
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])-1):
            temp = (matrix[i][j], matrix[i][j+1],
                    matrix[i+1][j], matrix[i+1][j+1])
            if temp not in s:
                s.add(temp)
    return len(s)
