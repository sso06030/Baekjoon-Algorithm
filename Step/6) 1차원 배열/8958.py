# OX퀴즈

def score():
    res = input()
    score = 0
    sum = 0
    for i in range(len(res)):
        if(res[i]=="O"):
            score += 1
            sum += score
        else:
            score = 0
    return sum
    
n = int(input())

for i in range(n):
    print(score())
