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