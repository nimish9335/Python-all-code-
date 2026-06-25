s=input("Enter the sentence:")

arr=s.split()
ans=""
maxi=0
for sen in arr:
    if len(sen)>maxi:
        ans=sen
        maxi=len(sen)

print(f"Longest part in this sentence:{ans}")