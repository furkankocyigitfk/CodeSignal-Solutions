def electionsWinners(votes, k):
    count = 0
    m = max(votes)

    if k == 0:
        if votes.count(m) != 1:
            return 0
        return 1

    for vote in votes:
        if vote + k > m:
            count += 1

    return count
