def myfun(n):
    if n == 0:
        return 1
    else:
        return n*myfun(n-1)


print(myfun(5))
