# 사분면 고르기

def quadrant(x,y):
    if(x>0):
        if(y>0):
            print(1)
        else:
            print(4)
    else:
        if(y>0):
            print(2)
        else:
            print(3)
    
x = int(input())
y = int(input())

quadrant(x,y)
