num1 = int(input("Enter your 1st Number: "))
num2 = int(input("Enter your 2nd Number: "))
num3 = int(input("Enter your 3rd Number: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num3)
else:
    print(num3)



#2nd Solution:= Withou any chochale bazzi

print(max(num1, num2, num3))