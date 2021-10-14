def avoidObstacles(arr):
    arrCount = [0] * (max(arr) + 2)

    for i in arr:
        arrCount[i] = 1

    for i in range(1, len(arrCount)):
        flag = True
        j = 0
        while flag and j < len(arrCount):
            if(arrCount[j] == 1):
                flag = False
            j += i

        if flag:
            return i
