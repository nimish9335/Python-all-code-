def printer(s):
    freq={}
    for i in range(len(s)):
        s[i]=s[i].lower()
        if s[i] in freq:
            freq[s[i]]+=1
        else:
            freq[s[i]]=1
    for key,value in freq.items():
        print(f"{key}={value}")
    return

sentence=list(input("Enter the sentence:").split())
printer(sentence)