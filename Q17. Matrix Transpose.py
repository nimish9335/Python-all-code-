n,m=map(int,input().split())

matrix=[]

for i in range(n):
    row=list(map(int,input(f"Enter {i}th row:").split()))
    matrix.append(row)

#declear the array with fixed size with value 0
ansmatrix=[[0]*n for _ in range(m)]
for i in range(n):
    for j in range(m):
        ansmatrix[j][i]=matrix[i][j]

print(f"original matrix:{matrix}")
print(f"final transpose of matrix:{ansmatrix}")

