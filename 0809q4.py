def removerepeats(l):
    for x in range(len(l) -1 , -1, -1):
        if l.count(l[x]) > 1:
            l.pop(x)
            
    print(l)

removerepeats([1,2,4,1])
removerepeats([1,1,2])