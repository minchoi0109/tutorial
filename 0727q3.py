def hasbalanceparan(s):
    if len(s) % 2 !=0:
        return False
    else:
        for x in range(0, int(len(s)/2)):
            if s[int(len(s)/2) - (x+1)] =="(" and s[int(len(s)/2)-x] == ")":
                return True
            else: 
                return False

print(hasbalanceparan("((()())())(("))