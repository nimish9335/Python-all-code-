s=input("Enter the string:")

ans=""
cnt=1
prev=s[0]
for ch in s:
    if ch==prev:
        cnt+=1
    else:
        ans+=prev
        ans+=str(cnt)
        cnt=1
        prev=ch

ans+=prev
ans+=str(cnt)

print(f"final compressed string:{ans}")