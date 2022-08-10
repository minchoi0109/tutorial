import copy

def median(a):
    
    b = copy.copy(a)
    a.sort()
    
    if len(a) == 0:
        return None
    
    elif len(a) % 2 != 0:
        result = a[len(a)//2]
        print(result)
    else:
        resultr = (a[int(len(a)/2) -1 ] + a[int(len(a)/2)]) / 2
        print(resultr)


median([1,2,3])