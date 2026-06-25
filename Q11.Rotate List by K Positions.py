arr=list(map(int,input("Enter the list:").split()))
k=int(input("Enter the value of K:"))

n=len(arr)

arr1=arr[:k+1]
arr2=arr[k+1:]
arr_final=arr2+arr1

print(f"final rotated arr:{arr_final}")