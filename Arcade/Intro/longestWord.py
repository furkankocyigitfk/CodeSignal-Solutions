def longestWord(text):
    arr = list()
    word = ""

    for c in text:
        if not c.isalpha():
            arr.append(word)
            word = ""
        elif c.isalpha():
            word += c
    arr.append(word)
    word = ""

    for i in range(len(arr)):
        if(len(arr[i]) > (len(word))):
            word = arr[i]

    return word
