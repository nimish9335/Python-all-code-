def printer(s):
    freq={}
    for ch in s:
        ch=ch.lower()
        if ch==' ':
            continue
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    
    for key,value in freq.items():
        print(f"{key,value}")
    return

sentence =input("Enter the string:")
printer(sentence)