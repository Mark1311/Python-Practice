num= int(input("Enter your Number"))

def myfun(num):
    if num<=1:
        return num
    else:
        return num * myfun(num-1)

if num == 0:
    print("Enter a Valid Number")
else:
    print(myfun(num))