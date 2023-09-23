X = [[1,2,3], [4,8,9], [7,8,2]]

Y = [[8,5,2], [7,9,6],[4,5,2]]

result =[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

print(result)


#Or

for i in result:
    print(i)