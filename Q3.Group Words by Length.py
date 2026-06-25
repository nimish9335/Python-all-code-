arr=list(input("Enter the list of words:").split())
n=len(arr)

map={}
for s in arr:
    m=len(s)
    if m in map:
        map[m].append(s)
    else:
        map[m]=[s]

for key, values in map.items():
    print(key,values)