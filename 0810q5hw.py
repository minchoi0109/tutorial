def issorted(a):
    new = a
    for i in range(0, len(a)-1):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    
    if new == a:
        return True
    else: 
        return False

print(issorted([4,2,3]))