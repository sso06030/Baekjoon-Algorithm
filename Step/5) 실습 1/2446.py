# 별 찍기 -9

n = int(input())

for i in range(1,2*n):
    if(i<=n):
        for j in range(i-1):
            print(" ",end="")
        for j in range((2*n+1)-i*2):
            print("*",end="")
        print()
    else:
        for j in range(2*n-i-1):
            print(" ",end="")
        for j in range(2*(i-n)+1):
            print("*",end="")
        print()
