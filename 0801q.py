def testmostcommonname(l):
    newlist = []
    if len(l) == 0:
        return False
        
        for x in range(0,len(l)-2):
            for y in range(1, len(l)-1):
                if l[x] == l[y]:
                    newlist.append(l[x])
    print(newlist)

testmostcommonname(["aaron","cindy","aaron","jane"])