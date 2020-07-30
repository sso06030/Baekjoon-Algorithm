# 알람 시계

# 45분 포함하기

def alarm(h,m):
    if(m>=45):
        print(h,m-45)
    else:
        if(h==0):
            h=23
            print(h,60-(45-m))
            
        else:
            print(h-1,60-(45-m))

h,m = input().split()

alarm(int(h),int(m))
