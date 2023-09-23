num = int(input("Enter your Number"))

if num < 0:
    print("enter positive number")

else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(sum)


# Print N natural Number

for i in range(0, 100):
    print(i)
