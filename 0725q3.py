def power(base, expt):
    if expt == 0:
        return 1
    else:
        return base * power(base, expt - 1)
print(power(2,6))

#in the fibonacci sequence, each element is the sum of two elements before if
#fib(3) --> 1, 1, 2      fib(6) --> 1,1,2,3,5,8

def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))