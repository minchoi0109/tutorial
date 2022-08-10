def getpairsum(l, target):
    for x in range(0, len(l)-1):
        for y in range(x+1, len(l)):
            if l[x] + l[y] == target:
                t =(l[x], l[y])
                return t
            else:
                return None

print(getpairsum([1,1,2],2))