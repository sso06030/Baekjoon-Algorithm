# 알파벳 찾기

alpha=[]
cnt=[]
for i in range(26):
    cnt.append(-1)
    alpha.append(chr(97+i))
    
str = input()


for i in range(len(str)):
    for j in range(26):
        if(str[i] == alpha[j]):
            if(cnt[j] == -1):
                cnt[j] = i

for i in range(26):
    print(cnt[i],end=" ")
