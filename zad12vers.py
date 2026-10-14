s="aabbcdd"
for i in range(len(s)):
    k=0
    for j in range(len(s)):
        if s[i]==s[j]:
            k+=1
    if k==1:
        print(s[i])