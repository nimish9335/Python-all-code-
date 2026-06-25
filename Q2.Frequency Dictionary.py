s=input("Enter the string:")
n=len(s)
map={}
for i in range(n):
    if s[i] in map:
        map[s[i]]+=1
    else : 
        map[s[i]]=1

for key,value in map.items():
    print(key,value)