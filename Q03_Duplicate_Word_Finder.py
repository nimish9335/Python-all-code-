def duplicate(s):
    freq={}
    ans=[]
    for word in s:
        word=word.lower()
        if word in freq:
            if word not in ans:
                ans.append(word)
        else:
            freq[word]=1
    
    if not ans:
        print("No duplicate words found")
    else:
        for word in ans:
            print(word)

sentence = input("Enter the sentence:").split()
duplicate(sentence)