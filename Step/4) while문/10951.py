# A+B -4

# try 블록 수행 중 오류가 발생하면
# except 블록이 수행됨

while(True):
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break
