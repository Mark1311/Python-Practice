"""Numb = int(input("Enter your Number"))
length = len(str(Numb))

sum = 0
temp = Numb

while temp > 0:
    digt = temp % 10
    sum += digt**length
    temp //= 10

if Numb == sum:
    print("yess...This is A armstrtong Numbeer")
else:
    print("this is not a Aramstrong Number")"""


# IN A Interval of Armstrong Number


for Numb in range(10, 50000):

    length = len(str(Numb))

    sum = 0
    temp = Numb

    while temp > 0:
        digt = temp % 10
        sum += digt**length
        temp //= 10

    if Numb == sum:
        print(Numb)
