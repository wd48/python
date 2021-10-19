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
