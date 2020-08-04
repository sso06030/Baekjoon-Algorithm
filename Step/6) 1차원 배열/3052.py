# 나머지

num=[]

for i in range(10):
    num.append(int(input()))

rest = []
rest.append(num[0]%42)

for i in range(1,10):
    n = num[i]%42
    for j in range(len(rest)):
        if(rest[j]==n):
            break
        if(j==len(rest)-1):
            rest.append(n)
            

print(len(rest))
