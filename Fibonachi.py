# Print Fibonachi Sequence
Num = int(input("Enter your Valur: "))

# Using SIMPLE Method:---------
a = 0
b = 1
if Num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1, Num+1):
        c = a+b
        a = b
        b = c
        print(c)

# Sum of Fibonachi Number--------


def fibo(N):
    if N < 0:
        print("Enter Valid Input")
    elif N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fibo(N-1) + fibo(N-2)


print(fibo(Num))
