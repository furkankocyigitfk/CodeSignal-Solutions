def isIPv4Address(s):
    a = s.split(".")
    if len(a) != 4:
        return False

    for x in a:
        if not x.isdigit():
            return False

        if (int(x) < 10 and len(x) > 1) or int(x) > 255:
            return False
    return True
