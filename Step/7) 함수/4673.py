# 셀프 넘버

# list in item : 리스트에 아이템이 존재하는지 확인

# 1~10000의 list 정의
a=[]
for i in range(1,10001):
    a.append(i)


# 셀프넘버가 10000보다 작고 list에 존재하면
# list에서 제거
def func(num):
    num = str(num)
    sum = 0
    
    for i in range(len(num)):
        sum += int(num[i])
    new = int(num)+sum
    
    if(new<=10000):
        if(new in a):
            a.remove(new)

for i in range(1,10001):
    func(i)


# 셀프넘버가 제거된 list 출력
for i in range(len(a)):
    print(a[i])
