arr1=list(map(int,input("Enter the first list:").split()))
arr2=list(map(int,input("Enter the first list:").split()))

map ={}
for num in arr1:
    if num in map:
        map[num]+=1
    else:
        map[num]=1

ans=[]
for num in arr2:
    if num in map:
        map[num]-=1
        ans.append(num)

print(f"Intersection in between these two array:{ans}")