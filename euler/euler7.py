#7번 문제
# 10,001번째 소수 구하기

# 소수 판별 함수
def is_prime_num(x):
    # 2부터 (x-1)까지
    for i in range(2, x):
        # x가 나눠지면 소수가 아니다
        if x % i == 0:
            return False
    return True # 나머지는 소수

# 체 이용 코드
from time import time

def eratos(num):
    sieve = [False, False] + [True] * num
    count = 0
    for i, val in enumerate(sieve):
        if val:
            count += 1
            sieve[i*2::i] = [False] * len(sieve[i*2::i])
            if(count == 10001):
                print(i)
                break
    
    return [i for i,x in enumerate(sieve) if x]


start_t = time()
li = eratos(150000)

print(time() - start_t)

# 체 이용 코드 2

number = 50
for i in range(1, number+1):
    if number%i == 0: # 나눠서 0이면 약수
        print(i)

# 소수 확인
# 나누어떨어지는 수가 하나라도 있으면 소수가 아니고 정지
number = 50
i=1
while i <= number:
    if number%i == 0:
        print("not prime")
        break
    i+=1

# 소수인지에 따라 T/F 반환시키는 함수
def is_prime(num):
    if num==1:
        return False
    i=2
    while i<num:
        if num%i == 0: # 나눠떠러진다 > 소수 아님 > 스탑
            return False
        i += 1
    return True

number = 10000

if is_prime(number):
    print("prime")
else:
    print("not prime")

# 합친 코드
def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i<num:
        if num%i == 0:
            return False
        i += 1
    return True
# 참일때
i = 1
pCnt = 0
while True:    
    if is_prime(i):
        pCnt += 1
        print(i," is prime factor")
    if pCnt == 10001:
        break
    i += 1

number = 8584038
i = 1
while i <= number:
    # number랑 i가 나눠떨어지고 is_prime 이 참일때
    if number%i == 0 and is_prime(i):
        print(i," is prime factor")
    i += 1