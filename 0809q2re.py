def median(a):
    n = []
    k = 0
    for x in range(1, len(a)):
        if a[k] < a[x]:
            n.append(a[k])
        else:
            for y in range(0, len(n)):
                if a[x] < a[n]:
                    n.insert(y, a[x])
                else:
                    n.append(a[x])
                    
 
    
    if len(n) == 0:
        return None
    
    elif len(n) % 2 != 0:
        result = n[len(n)//2]
        print(result)
    else:
        resultr = (n[int(len(n)/2) -1 ] + n[int(len(n)/2)]) / 2
        print(resultr)


median([1,2,3])