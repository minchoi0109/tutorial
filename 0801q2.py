def isanagram(s1, s2):
    dictionary = dict()
    dic2 = dict()
    for char in s1:
        if (dictionary.get(char, 0)) == 0:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    for char in s2:
        if (dic2.get(char, 0)) == 0:
            dic2[char] = 1
        else:
            dic2[char] += 1
    
    if dictionary == dic2:
        return True
    else:
        return False
            