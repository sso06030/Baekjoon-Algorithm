# 최댓값

# list 미리 선언하기
# list 마지막에 원소 추가 : list.append(item)

num = []
for i in range(9):
    num.append(int(input()))

max = num[0]
for i in range(1,9):
    if(num[i] > max):
        max = num[i]

print(max)
for i in range(9):
    if(num[i]==max):
        print(i+1)
    

