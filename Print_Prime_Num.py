Str = int(input("Enter your Starting Value "))
End = int(input("Enter your Ending Value "))

for i in range(Str, End + 1):
    if i > 1:
        for num in range(2, i):
            if(i % num) == 0:
                break
        else:
            print(i)
