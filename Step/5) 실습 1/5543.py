# 상근날드

def min(n):
    item = []
    for i in range(n):
        tmp = int(input())
        item.append(tmp)

    min = item[0]
    for i in range(1,n):
        if(item[i]<min):
            min = item[i]

    return min

burger = min(3)
coke = min(2)

print(burger+coke-50)
