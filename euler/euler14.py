# 백만 이하로 시작하는 우박수 중 가장 긴 과정을 거치는 것은?
# Longest Collatz sequence

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