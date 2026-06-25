arr=list(map(int,input("Enter the list :").split()))

ans=[]
for num in arr:
    if num%2==0:
        ans.append(num*num)

print(ans)