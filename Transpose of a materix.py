# convert row into colume that is called transporse

#Soln -1 Using for loop.

A = [[1,2,3],[4,5,6]]

T = [[0,0], [0,0], [0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        T[j][i] = A[i][j]

print(T)  #This is print your materix

#OR

for i in T:    #This is print your itrable materix
    print(i)