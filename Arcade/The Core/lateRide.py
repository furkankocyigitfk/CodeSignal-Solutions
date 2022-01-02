def solution(n):
    h = n // 60
    m = n - h * 60

    return sum(list(map(int, str(h)))) + sum(list(map(int, str(m))))
