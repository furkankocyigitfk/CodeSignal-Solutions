def lineEncoding(s):
    curr_char = s[0]
    curr_count = 0

    ss = ""
    for c in s:
        if curr_char != c:
            if curr_count > 1:
                ss += str(curr_count) + curr_char
            else:
                ss += curr_char

            curr_count = 1
            curr_char = c
        else:
            curr_count += 1

    if curr_count > 1:
        ss += str(curr_count) + curr_char
    else:
        ss += curr_char

    return ss
