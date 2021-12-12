def messageFromBinaryCode(code):
    arr = [code[i:i+8] for i in range(0, len(code), 8)]
    return "".join(chr(int(c, 2)) for c in arr)