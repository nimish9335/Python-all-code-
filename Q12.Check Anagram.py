s1=input("Enter first string :")
s2=input("Enter second string :")

map={}
for ch in s1:
    if ch in map:
        map[ch]+=1
    else:
        map[ch]=1

for ch in s2:
    if ch in map:
        map[ch]-=1
    else:
        print("False")
        exit()
        
print("true")