#What is Punctuation.

# Special character of my keyboard that is called this.
#Like:= :, ., /, ?, etc.

punch = """1234567890-=#$^[[()![]{}//<>*-+~`?"""

mystr = input("enter your string")

temp = ""

for i in mystr:
    if i not in punch:
        temp = temp + i
     
print(temp)