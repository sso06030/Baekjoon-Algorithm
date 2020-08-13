# 다이얼

def check(n):
    if(65<=n<=67):
        return 3
    elif(68<=n<=70):
        return 4
    elif(71<=n<=73):
        return 5
    elif(74<=n<=76):
        return 6
    elif(77<=n<=79):
        return 7
    elif(80<=n<=83):
        return 8
    elif(84<=n<=86):
        return 9
    elif(87<=n<=90):
        return 10

word = list(input())
time=0

# 아스키코드 -> 숫자 : ord()
for i in range(len(word)):
    word[i] = ord(word[i])
    time += check(word[i])
    

print(time)
