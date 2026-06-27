def PrimeNumberPrinter(l,r):
    arr=[]
    for i in range(l,r+1):
        x=True
        for j in range(2,i):
            if i%j==0:
                x=False
                break
        if x:
            arr.append(i)
    
    print(f"List of prime number in this range l and r:{arr}")

l=int(input("Enter the left boundary:"))
r=int(input("Enter the right boundary:"))

PrimeNumberPrinter(l,r)