def rangesum(lo,hi):
    if lo > hi:
        return 0
    else:
        return lo + rangesum(lo+1, hi)

print(rangesum(2,4))
