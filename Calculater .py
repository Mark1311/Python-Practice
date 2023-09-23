num1 = int(input("Enter your First Number"))
num2 = int(input("Enter your Secondery Number"))

choise = input("Enter your Operation")

if choise == "+":
    print(num1 + num2)

elif choise == "-":
    print(num1 - num2)

elif choise == "*":
    print(num1 * num2)

elif choise == "/":
    print(num1 / num2)

elif choise == "%":
    print(num1 % num2)

elif choise == "//":
    print(num1 // num2)

else:
    print("Enter a Valid Operatipns")
