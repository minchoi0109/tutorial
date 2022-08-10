def mostcommonname(l):
    dictionary = dict()
    new = set()
    count = 0
    item = ""
    if len(l) == 0:
        return False
    else:
        for x in l:
            if dictionary.get(x, 0) == 0:
                dictionary[x] = 1
            elif dictionary.get(x, 0) != 0:
                dictionary[x] = dictionary[x] + 1
        for y in dictionary:
            if dictionary[y] > count:
                count = dictionary[y]
                item = y
        for z in dictionary:
            if dictionary[z] == count:
                new.add(z)
        
        return new
    #print(new)

print(mostcommonname(["a","b","a","c","b"]))