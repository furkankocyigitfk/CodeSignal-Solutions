def variableName(name):
    if not name[0].isalpha() and name[0] != "_":
        return False

    for i in range(0, len(name)):
        if not name[i].isalnum() and name[i] != "_":
            return False

    return True
