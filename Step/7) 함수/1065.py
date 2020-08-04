# 한수

n = int(input())
cnt=0


def hansu(n):
    n = str(n)

    # 숫자가 100보다 작은 수는 전부 한 수
    if(int(n)<100):
        return "ab"

    # 공차 구하기
    else:
        gap = int(n[0])-int(n[1])

    # 각 자릿수의 공차 비교
    for i in range(1,len(n)-1):
        if(int(n[i])-int(n[i+1])!=gap):
            break
        if(i==len(n)-2):
            return "ab"


for i in range(1,n+1):
    a = hansu(i)
    if(a == "ab"):
        cnt +=1
    
print(cnt)

