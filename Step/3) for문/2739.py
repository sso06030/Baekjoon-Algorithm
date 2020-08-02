#구구단

#range(시작 숫자, 끝 숫자+1)

def gugudan(n):
    for i in range(1,10):
        print(f"{n} * {i} = {n*i}")

n = int(input())
gugudan(n)
