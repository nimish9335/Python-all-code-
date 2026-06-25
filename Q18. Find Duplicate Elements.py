arr=list(map(int,input("Enter the list of numbers:").split()))

map={}
for num in arr:
    if num in map:
        map[num]+=1
    else:
        map[num]=1

ans=[]
for key,value in map.items():
    if value>1:
        ans.append(key)

print(f"Final duplicate array:{ans}")