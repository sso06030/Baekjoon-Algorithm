# 평균은 넘겠지

# round(실수,n) : 실수의 소수점을 n번째 까지 반올림하여 표현함
# format(실수,"포맷 지정자") : 포맷 지정자에 맞게 숫자를 표현함

cnt = int(input())

for j in range(cnt):
    stu = list(map(int,input().split()))


    sum = 0
    for i in range(1,len(stu)):
        sum += stu[i]
    avg = sum/stu[0]


    n = 0
    for i in range(1,len(stu)):
        if(stu[i]>avg):
            n+=1

    rate = format(n/stu[0]*100,".3f")

    print(str(rate)+"%")
