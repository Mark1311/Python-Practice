def myfun(num):
    if num>1:
        myfun(num//2)
    print(num%2, end ="")

myfun(15)