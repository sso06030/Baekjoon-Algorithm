#문자열 반복


cnt = int(input())


def func(n,string):
    for i in range(len(string)):
        for j in range(n):
            print(string[i],end="")
    print()
        
for i in range(cnt):
    n,string = input().split()
    func(int(n),string)
