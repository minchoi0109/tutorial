def mostcommonname(l):
    dictionary = dict()
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
        return item
print(mostcommonname([2,5,3,4,6,4,2,4,5]))