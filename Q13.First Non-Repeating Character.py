s=input("Enter a string:")

map={}
for ch in s:
    if ch in map:
        map[ch]+=1
    else:
        map[ch]=1

for key,value in map.items():
    if value==1:
        print(f"first char:{key}")
        exit()

print("-1")