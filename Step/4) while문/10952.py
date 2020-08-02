# A+B -5

def plus(a,b):
    return a+b

a,b = map(int,input().split())

while(a!=0 and b!=0):
    print(plus(a,b))
    a,b = map(int,input().split())
