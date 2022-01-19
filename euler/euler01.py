# # 1번 문제
answer = 0
for n in range(1,1000):
    if n%3 == 0 or n%5 == 0:
        answer += n
print(answer)

# 다른 풀이

# 함수 선언
def q1(x):
    num = 1
    sum = 0

    while num < x :
        if num % 3 == 0 :
            sum += num
        elif num % 5 == 0 :
            sum +=  num
        num += 1
    return sum
# 입력값 받음
input_console = int(input('Enter a natural num : '))
# 입력값을 함수에 돌려 결과값 출력
print(q1(input_console))
