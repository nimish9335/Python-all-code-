sentence=input("Enter the sentence:")
arr=sentence.split()

d={}
for word in arr:
    if word in d:
        d[word]+=1
    else:
        d[word]=1

print(f"Print final output:{d}")