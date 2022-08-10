def smallestdifference(a):
    newlist = []
    if len(a) == 0:
        return -1

    for x in range(0, len(a)-1):
        for y in range( x + 1, len(a)):
            if a[x] >= a[y]:
                newlist.append(a[x] - a[y])
            else:
                newlist.append(a[y] - a[x])
    
    print(min(newlist))

smallestdifference([19,2,83,6,27])
