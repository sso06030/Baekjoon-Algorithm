# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

# 숫자를 문자열로 변환하여 인덱스로 접근
res = str(a*b*c)
num = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(res)):
    for j in range(10):
        # 문자 하나하나를 숫자로 변환하여 비교
        if(int(res[i])==j):
            num[j] = num[j]+1


for i in range(10):
    print(num[i])
    
