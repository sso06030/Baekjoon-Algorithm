#나머지

def cal(A,B,C):
    print((A+B)%C)
    print(((A%C) + (B%C))%C)
    print((A*B)%C)
    print(((A%C) * (B%C))%C)

a,b,c = input().split()

cal(int(a),int(b),int(c))
