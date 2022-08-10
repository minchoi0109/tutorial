def alternatingsum(a):
    s = 0
    if len(a) == 0:
        return 0
    else:
        for p in range(0, len(a)):
            if p % 2 == 0:
                s += a[p]
            else: 
                s -= a[p]
    print(s)
 

alternatingsum([5,3,8,4])
