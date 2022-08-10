print(4/2)


def median(a):
    a.sort()
    if len(a) % 2 != 0:
        result = a[len(a)//2]
        print(result)
    else:
        resultr = (a[int(len(a)/2) -1 ] + a[int(len(a)/2)]) / 2
        print(resultr)


median([6,7,2,8,3])
median([3,1,4,9,2,5,3,6])