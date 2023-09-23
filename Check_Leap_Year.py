Year = int(input("Enter A Valid Yera"))

if (Year % 400 == 0) and (Year % 100 == 0):
    print("This is A Leap Yera")

elif(Year % 4 == 0) and (Year % 100 != 0):
    print("This is A Leap Yera")

else:
    print("This is not a Leap Year")


# This Code for Check A Leap Yera.....!!!
