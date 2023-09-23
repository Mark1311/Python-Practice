#Sol:= 1 Using Enumerate method 


lst = ["A", 'B', 'C', 'D', 'E', 'F']

for index, value in enumerate(lst, start = 1 ):
    print(value, index)



#Soln := 2 Without enmuerated mathod

for i in range(len(lst)):
    print(i, lst[i])