n=int(input("Enter the size of dictionary:"))

d={}
for i in range(n):
    key=str(input("Enter the key:"))
    value=int(input("Enter the value of key:"))
    d[key]=value

sorted_d = dict(sorted(d.items(), key=lambda x: x[1]))

print(sorted_d)