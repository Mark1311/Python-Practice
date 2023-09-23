num = input("Enter Your String")

def myfun(num):
    try:
        float(num)
        return True
    except:
        return False
    
print(myfun(num))