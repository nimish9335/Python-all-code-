def count_vowel(s):
    n=len(s)
    cnt=0
    for ch in s:
        if ch in "aeiou":
            cnt+=1

    return cnt

s=input("Enter the string :")
ans=count_vowel(s)
print(f"Number of vowel present in s:{ans}")