def checkpalindrome(s):
    temp=s[::-1]
    if(s==temp):
        return True
    else:
        return False

s=input("Enter the string:")
ans=checkpalindrome(s)
if(ans):
    print(f"String is palindrome:{s}")
else:
    print(f"String is not a palindrome:{s}")