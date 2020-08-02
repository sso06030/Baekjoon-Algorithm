# 빠른 A+B

## for문 문제를 풀기 전에 주의해야 할 점
# 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다.
# Python : input 대신 sys.stdin.readline을 사용하여 시간을 단축할 수 있다.

import sys

def plus(a,b):
    print(a+b)

t = int(sys.stdin.readline())

for i in range(t):
    a,b = sys.stdin.readline().split()
    plus(int(a),int(b))
