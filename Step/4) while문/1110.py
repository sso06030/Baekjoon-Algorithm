# 더하기 사이클

# new를 구한 후 비교하며 while 루프 돌리기
# 불필요한 변수 줄이기


n = int(input())
cnt = 0
new = n

while(True):
    n1 = int(new/10)
    n2 = new%10
    
    p = n1+n2
    
    new = (n2*10)+(p%10)
    cnt = cnt+1
    
    if(new == n):
        break

print(cnt)
