arr = list(map(int, input("Enter the list:").split()))
print(arr)

maxi=arr[0]
for num in arr:
    if(num>maxi):
        maxi=num

secondmaxi=-1
for num in arr:
    if(num<maxi and num>secondmaxi):
        secondmaxi=num

print(f"second largest element {arr} in this list: {secondmaxi}")