# 17번
# 숫자를 알파벳으로 변환하고 글자수를 세는 문제

# 1 정석

# 딕셔너리
data1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
data2='''one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety'''
numbers=dict(zip(data1,data2.split()))

# dict() 딕셔너리 타입생성
# zip() 나열형의 자료형 2개를 짝으로 만들어 묶어준다

# total=0
# for i in range(1,21):
    # total += len(numbers[i])
    # print(i, numbers[i], len(numbers[i]), total)

# 100까지 출력
# def func(num):
#     if (num) not in numbers:
#         numbers[num] = numbers[num - num % 10] + numbers[num % 10]
#     return numbers[num]

# total=0
# for i in range(1,100):
#     value=func(i)
#     total += len(value)
#     print(i, value, len(value), total)

# 1000까지 계산

def func(n):
    if n <100:
        if (n) not in numbers:
            numbers[n] = numbers[n - n % 10] + numbers[n % 10]
        return numbers[n]
    if n <1000:
        if n==0:
            return numbers[n//100] + numbers[100]
        return numbers[n//100] +  numbers[100] + 'and' + numbers[n % 100]
    return 'one' + numbers[1000]
 
total = 0
for i in range(1,1001):
    value = func(i)
    total += len(value)
    print(i, value, len(value), total)