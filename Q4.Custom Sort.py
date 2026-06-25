arr=list(input("Enter the list of words:").split())

arr.sort(key=lambda s :(len(s),s))
print(arr)