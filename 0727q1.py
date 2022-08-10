def nthadditiveprime(n):
    list = []
    for x in range(2, n // 2):
        if n % x != 0:
            for y in range(0, len(str(n))):
                list.append(int(str(n)[y]))
            for z in range(2, sum(list)//2):
                if sum(list) % z != 0:
                    print(sum(list))



nthadditiveprime(113)
