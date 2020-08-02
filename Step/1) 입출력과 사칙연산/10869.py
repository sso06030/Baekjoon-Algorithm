#사칙연산

# / : 나누기
# // : 나누기 연산 후 소수점 이하의 수를 버림

def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a//b)
    print(a%b)

a,b = input().split()
cal(int(a), int(b))
