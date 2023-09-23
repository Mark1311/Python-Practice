# num = int(input("Enter your Number"))


# def myfun(num):
#     if num <= 1:
#         return num
#     else:
#         return myfun(num-1) + myfun(num-2)


# if num <= 0:
#     print("enter positive num")

# else:
#     for i in range(num):
#         print(myfun(i))


# 2nd Method

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


for i in range(9):
    print(fibo(i))
