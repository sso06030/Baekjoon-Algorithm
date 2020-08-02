# X보다 작은 수

# map함수 : map(적용시킬 함수, 적용할 요소들)
# list함수 : list 형태로 저장

n,x = map(int,input().split())

a = list(map(int,input().split()))

for i in range(n):
    if(a[i]<x):
        print(a[i],end=" ")
    
