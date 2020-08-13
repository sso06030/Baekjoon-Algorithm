# 크로아디아 알파벳

word = input()
cnt=0

for i in range(len(word)):
    if(word[i]=='='):
        if(word[i-1]=='c' or word[i-1]=='z' or word[i-1]=='s'):
            cnt+=1
        if(word[i-1]=='z' and word[i-2]=='d'):
            cnt+=1
    elif(word[i]=='j'):
        if(word[i-1]=='l' or word[i-1]=='n'):
            cnt+=1
    elif(word[i]=='-'):
        if(word[i-1]=='c' or word[i-1]=='d'):
            cnt+=1

print(len(word)-cnt)
