st=input("Enter a string :")

n=len(st)
cnt_vowel=0
for i in range(n):
    # this give indexing of string 
    if st[i]=='a' or st[i]=='e' or st[i]=='i' or st[i]=='o' or st[i]=='u': cnt_vowel+=1

print("total cnt of vowel", st,  "in this string:", cnt_vowel)
