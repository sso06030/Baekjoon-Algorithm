# 윤년

def leap_year(year):
    if(year%4==0):
        if(year%100!=0 or year%400==0):
            print(1)
        else:
            print(0)
    else:
        print(0)

year = int(input())
leap_year(year)
