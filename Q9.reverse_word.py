s=input("Enter the string:")
reverse_s=""
i=len(s)-1
while i>=0:
    reverse_s+=s[i]
    i-=1

print(f"reverse of this string {s} is {reverse_s}")