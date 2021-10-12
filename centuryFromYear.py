def centuryFromYear(year):
    if year // 100.0 == year / 100:
        return year / 100
    return year // 100 + 1
