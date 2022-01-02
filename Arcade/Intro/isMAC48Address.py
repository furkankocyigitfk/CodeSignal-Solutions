def isMAC48Address(s):
    if len(s) != 17:
        return False

    arr = s.split("-")

    if len(arr) != 6:
        return False
    try:
        x = [int(h, 16) for h in arr]
    except Exception as e:
        print(e)
        return False

    return True
