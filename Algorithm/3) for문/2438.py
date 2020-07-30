# 별 찍기 -1

# 줄바꿈 없이 출력하는 방법
# print(str, end="")

n = int(input())

for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print()
    
