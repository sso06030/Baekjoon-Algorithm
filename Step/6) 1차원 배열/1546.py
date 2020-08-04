# 평균

cnt = int(input())


num = list(map(int,input().split()))

max = max(num)

for i in range(cnt):
    num[i] = num[i]/max*100

sum = 0
for i in range(cnt):
    sum = num[i]+sum

print(sum/cnt)
