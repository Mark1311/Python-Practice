num = int(input("Enter your Natural Number"))

def myfun(num):
    if num<=1:
        return num
    else:
          return num + myfun(num-1)

print(myfun(num))