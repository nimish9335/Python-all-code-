def remove_dulicate(arr):
    ans=[]
    s=set()
    for num in arr:
        s.add(num)

    for num in s:
        ans.append(num)
    
    return ans

arr=list(map(int,input("Enter the list of element:").split()))
ans=remove_dulicate(arr)
print(f"final_arr:{ans}")