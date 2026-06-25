s=input("Enter a string:")

map={}
for ch in s:
    if ch in map:
        map[ch]+=1
    else:
        map[ch]=1

maxi=0
for values in map.values():
    if values>maxi:
        maxi=values

for key,values in map.items():
    if(values==maxi):
        print(key)