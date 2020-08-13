# 단어 공부

# 한 줄로 for문 돌려서 원하는 값으로 리스트 채우기
cnt = list(0 for i in range(26))
alpha = list(chr(65+i) for i in range(26))

# 대문자로 변환
string = input().upper()

# 문자 하나씩 알파벳과 비교해서 카운트 세기
for i in range(len(string)):
    for j in range(26):
        if(string[i] == alpha[j]):
            cnt[j]+=1

# 가장 많이 나온 문자의 횟수 구하기
max_V = max(cnt)

check=[]
# for문 돌려서 max횟수와 같은 문자 check[]에 추가
for i in range(26):
    if(cnt[i]==max_V):
        check.append(i)

# check[]의 수에 따라 출력 다르게
if(len(check)>1):
    print("?")
else:
    print(alpha[check[0]])
