#최초 풀이
def listsum(l):
    n = 0
    sum = 0
    if len(l) < n:
        return "stop"
    else:
        sum += l(n)
        return listsum(n + 1)
print(listsum([2,3,5,7,11]))


#정답
def listsum(l):
    if (len(l) == 0):
        return 0
    else: 
        return l[0] + listsum(l[1:])

print(listsum([2,3,5]))