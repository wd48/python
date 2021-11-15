# 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?
# Longest Collatz sequence
# 어떤 특수한 규칙으로 1로 수렴하는 수열이 있는데, 백만까지의 수를 대입했을때, 수열의 길이가 가장 긴 수를 찾는 문제입니다.

# 짝수일때 2로 나누고
# 홀수면 *3 +1
def collatz(n):
    if n == 1: return
    elif n%2==0:
        return n/2
    else:
        return n*3+1

print(collatz(13))

# 수열 생성
def collatz(n):
    print("while문 바깥 ",n)
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        print("else 아래 ",n)
    return
print(collatz(13))

# 수열생성 재귀호출
def collatz(n):
    print(n)
    if n == 1: return
    elif n%2==0:
        collatz(n/2)
    else:
        collatz(n*3+1)

collatz(13)


# 수열 count
def collatz2(n):
    count=1
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        count+=1
    return count

collatz2(13)
print(collatz2(13))

# 재귀호출 count
# 1 매개변수로 넘기면서 누적
# 2 리턴받는 시점에 누적
def collatz(n):
    if n==1: return 1
    elif n%2==0:
        return collatz(n/2) +1
    else:
        return collatz(n*3+1) +1

print(collatz(13))

# 메인 루프문으로 적용
def collatz(n):
    count=1
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        count+=1
    return count

i=1;maxVal=0

while i<100:
    val = collatz(i)
    if val>maxVal :
        maxVal = val
        print(i, maxVal)
    i+=1

# 루프 100만까지...
import time
start_time = time.time()

def collatz(n):
    count=1
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        count+=1
    return count

i=1;maxVal=0

while i<1000000:
    val = collatz(i)
    if val>maxVal :
        maxVal = val
    i+=1
print(maxVal)
print("calculation time: ",time.time()-start_time)

# 같은 방식
import time
start_time = time.time()

def collatz(n):
    if n == 1: return 1
    elif n%2==0:
        return collatz(n/2) +1
    else:
        return collatz(n*3+1) +1

i=1;maxVal=0

while i<1000000:
    val = collatz(i)
    if val>maxVal :
        maxVal = val
    i+=1
print(maxVal)
print("calculation time: ", time.time()-start_time)

# 속도 개선
# 루프마다 중복된 계산을 실행하기 때문에 느리다
# 방법
# 중복된 계산값을 메모리에 저장하고 시간 절약하는 다이나믹 프로그래밍(Dynamic Programming)

# 루프값 10 = cache{13:10} < 딕셔너리 타입 변수에 저장
# 불러낼 때는 cache[13]
# cache : 모든 결과값을 저장하므로 계산이 진행될수록 점점 커짐

import time
start_time = time.time()

def collatz(n):
    count=1
    while n != 1:
        # 수열만들면서 저장값 확인
        if (n) in cache :
            # 저장값이 있으면 저장된 값으로 대체
            count += cache[n]-1
            n = 1
        else :
            if n%2 == 0:
                n=n/2
            else:
                n=n*3+1
            count+=1
    return count

cache={}
i=1;maxVal=0

while i<1000000:
    val = collatz(i)
    if val > maxVal :
        maxVal = val
        starting = i
    cache[i] = val
    i+=1

print(maxVal)
print(val)
print(starting)
print("calculation time: ", time.time()-start_time)

#Generating Collatz sequence 
def collatz(n): 
    # 값을 담는 리스트 seq
    seq=[n] 
    while n!=1: 
        if n%2 ==0: 
            n=n/2 
            seq.append(n) 
        else: 
            n=3*n+1 
            seq.append(n) 
    return seq 

max_length = 1 
for i in range(1,1000000): 
    if max_length < len(collatz(i)): 
        max_length=len(collatz(i)) 
        starting=i 
        
print(starting, max_length)

## ref
# 한번의 싸이클
def hail(n):
    if n%2==0 : n=n/2
    else : n=3*n+1
    return n
# 싸이클을 몇번 반복하는지
def count(n):
    cnt=0
    while n>1:
        cnt+=1
        n=hail(n)
    return cnt
# 싸이클 횟수가 최대인 항 찾기
list=[]
for i in range(1,1000001):
    list.append(count(i))

m=max(list)
k=list.index(m)

#답
print(k+1)