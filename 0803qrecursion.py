def listsum(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + listsum(l[1:])

listsum([1,2,3,4,5])