def rotateImage(arr):
    newArr = []

    for i in range(len(arr)):
        temp = []

        for j in range(len(arr)):
            temp.append(arr[len(arr)-j-1][i])
        newArr.append(temp)

    return newArr
