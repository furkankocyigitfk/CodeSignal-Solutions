def validTime(time):
    time = list(map(int, time.split(":")))

    if time[0] > 23 or time[1] > 59:
        return False
    return True
