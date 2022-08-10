def f(n):
    if n == 0:
        return "boo"
    else:
        print(n)
        return f(n - 1)
print(f(5))