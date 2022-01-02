def solution(min1, min2_10, min11, s):
    c = 0

    if (s - min1 >= 0):
        s = s - min1
        c = c + 1

    temp = s // min2_10

    if(temp > 9):
        s = s - 9 * min2_10
        c = c + 9

        if (s > 0):
            c = c + s // min11
    else:
        s = s - temp * min2_10
        c = c + temp

    return c
