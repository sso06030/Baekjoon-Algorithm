# 두 수 비교하기

def compare(a,b):
    if(a==b):
        print("==")
    elif(a<b):
        print("<")
    else:
        print(">")
    
a,b = input().split()

compare(int(a), int(b))
