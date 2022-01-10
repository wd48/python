
# 다음은 달력에 관한 몇 가지 일반적인 정보입니다 (필요한 경우 좀 더 연구를 해 보셔도 좋습니다).

# 1900년 1월 1일은 월요일이다.
# 4월, 6월, 9월, 11월은 30일까지 있고, 1월, 3월, 5월, 7월, 8월, 10월, 12월은 31일까지 있다.
# 2월은 28일이지만, 윤년에는 29일까지 있다.
# 윤년은 연도를 4로 나누어 떨어지는 해를 말한다. 하지만 400으로 나누어 떨어지지 않는 매 100년째는 윤년이 아니며, 400으로 나누어 떨어지면 윤년이다

# 20세기 (1901년 1월 1일 ~ 2000년 12월 31일) 에서, 매월 1일이 일요일인 경우는 총 몇 번입니까?



# 1) 연,월,일 루프문 3개 중첩
# 2) 루프문 사이에 윤달 조건 추가
# 3) 최종 카운트 시 날짜가 1일이고 요일이 일요일인지 판단해서 카운트

# 요일: 1900년 1월 1일 월요일 = 0
# 날짜 총합해서 7로 나눠서 6이 나올때가 일요일임

daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0

for y in range(1900,2001):
    for m in range(12):
        for d in range(daylist[m]):
            total+=1
 
print(total)

# 윤달 조건문
# 4년마다 윤달 때문에 하루가 길어져서
# 4년마다 2월달에 하루씩 추가함 (m=1)
daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
total=0

for y in range(1900,2001):
    for m in range(12):
        day=daylist[m]
        if y%4==0 and m==1:
            day+=1
        for d in range(day):
            total+=1

print(total)


# 요일 계산 : 일요일
# 7로 나눠서 일요일인 날만 출력한 결과
daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0

for y in range(1900, 2001):
    for m in range(12):
        day=daylist[m]
        if y%4==0 and m==1:
            day+=1
        for d in range(day):
            if total%7==6:
                print(y, m+1, d+1)
            total+=1
print(total)


# 요일 카운트

daylist = [31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
count = 0

for y in range(1900, 2001):
    for m in range(12):
        day=daylist[m]
        if y%4==0 and m==1:
            day+=1
        for d in range(day):
            if y>1900 and d==0 and total%7==6:
                count+=1
            total+=1
print(total, count)