# 별 찍기 -13

# for i in reversed(range()) : for문 숫자 감소시키기

n = int(input())

def star(n):
    for i in range(1,2*n):
        if(i<=n):
            for j in range(i):
                print("*",end="")
            print()
        else:
            for j in reversed(range(2*n-i)):
                print("*",end="")
            print()

star(n)
