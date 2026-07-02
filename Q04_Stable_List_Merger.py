def solve(l1,l2):
    ans=[]
    for num in l1:
        ans.append(num)
    for num in l2:
        if num not in ans:
            ans.append(num)
    
    return ans

list1=list(map(int,input("Enter the list1:").split()))
list2=list(map(int,input("Enter the list2:").split()))

result=solve(list1,list2)
print(result)