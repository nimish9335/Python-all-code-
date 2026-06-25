arr=list(map(int,input("Enter the list of number:").split()))

ans=[]
map={}
for num in arr:
    if num in map:
        continue
    else:
        ans.append(num)
        map[num]=1

print(f"final result of this arr is:{ans}")