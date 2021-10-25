# 10번
# 2백만까지 소수의 총합
from re import T
from sympy import isprime

total = 0
i = 1
while i < 2000000:
    if isprime(i):
        total += i
    i += 1
print(total)


# 다른 풀이
from math import sqrt

# 판별함수 선언
def ChkPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

# 소수 카운트, 합계 저장
CntPrime = 1
SumPrime = 0

# 200만 소수 확인
while CntPrime <= 2000000:
    CntPrime += 1
    if ChkPrime(CntPrime) == True:
        SumPrime += CntPrime
print(SumPrime)

# ref. 2

# 소수를 담을 list 선언
a = []
# 200만 이하의 소수판별 이중 for문 
for i in range(2000001):
    result = True
    # 소수 : 1을 제외하므로 False
    if(i<2):
        result = False
    # 
    for j in range(2, i):
        if i%j == 0:
            result = False
    if result:
        a.append(i)

print(sum(a))