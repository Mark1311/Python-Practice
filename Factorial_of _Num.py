# Find Factorial of given Number....!!!

Num = int(input("Enter Your Number"))

# Using For Loop:----

Fact = 1

if Num < 0:
    print("Not will be find")
if Num == 0:
    print(1)
if Num > 0:
    for i in range(1, Num+1):
        Fact = Fact * i
print(Fact)


# Using Recursion

def factorial(a):
    if a == 0:
        return 1
    else:
        return (a*factorial(a-1))


res = factorial(Num)
print(res)
