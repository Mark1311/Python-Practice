A = [[1,2,3],[4,5,6],[7,8,9]]

B = [[9,8,7],[6,5,4],[3,2,1]]

res = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(B)):
        res[i][j] = A[i][j] + B[i][j]

print(res)

#Or

for i in res:
    print(i)