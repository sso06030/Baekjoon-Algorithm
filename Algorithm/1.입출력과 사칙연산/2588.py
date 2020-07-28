# 곱셈

def mul(n1,n2):
    n2_a = int(n2[2])
    n2_b = int(n2[1])
    n2_c = int(n2[0])
    
    a = n1*n2_a
    print(a)
    b = n1*n2_b
    print(b)
    c = n1*n2_c
    print(c)
    
    print(a+(b*10)+(c*100))

    

n1 = input()
n2 = input()
mul(int(n1),n2)
