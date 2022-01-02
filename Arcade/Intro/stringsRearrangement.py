from itertools import permutations


def stringsRearrangement(arr):
    perms = permutations(arr)
    for perm in perms:
        x = 0
        for i in range(len(perm)-1):
            y = getDistance(perm[i], perm[i+1])
            if y != 1:
                x += len(arr)
            else:
                x += y

        if x == len(arr) - 1:
            return True

    return False


def getDistance(s1, s2):
    dist = 0

    for i in range(len(s1)):
        dist += ord(s1[i]) != ord(s2[i])

    return dist
