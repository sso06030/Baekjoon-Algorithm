# 별 찍기 -21

n = int(input())

for i in range(n*2):
    if(i%2!=0):
        for j in range(n):
            if(j%2!=0):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    else:
        for j in range(n):
            if(j%2!=0):
                print(" ",end="")
            else:
                print("*",end="")
        print()
        
