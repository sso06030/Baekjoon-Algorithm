# 세 수 (두 번쨰로 큰 정수 출력)

# sort() : 리스트를 정렬 후
# del list[index] : 리스트 인덱스를 이용하여 가장 작은 수를 제거 하고
    ## remove(item) : 아이템 지정해서 삭제
# 가장 앞에 있는 수를 출력

num = list(map(int,input().split()))

num.sort()
del num[0]

print(num[0])    
