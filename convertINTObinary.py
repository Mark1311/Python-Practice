# Using Recursion

def myfun(n):
    if n > 1:
        myfun(n//2)
    print(n % 2, end="")


myfun(5)
