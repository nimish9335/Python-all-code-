arr=list(map(int,input("Enter the list of the element:").split()))

n=len(arr)
sum=n*(n+1)/2
arr_sum=0
for num in arr:
    arr_sum+=num

print(f"missing number in this array :{int(arr_sum-sum)}")