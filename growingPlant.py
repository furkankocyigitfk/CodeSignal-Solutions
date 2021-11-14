def growingPlant(upSpeed, downSpeed, desiredHeight):
    i = 1

    while desiredHeight > upSpeed and desiredHeight > 0:

        desiredHeight = desiredHeight - upSpeed + downSpeed
        i += 1

    return i
