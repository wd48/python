# 피보나치 수열에서 짝수이면서 4백만 이하인 값을 모두 더하기

# 1. 피보나치 수열 점화식
# 함수
def fibo(x):
    # 1,2일 때는 그대로
    if x==1 or x==2:
        return x
    else:
        return fibo(x-1)+fibo(x-2)
        
fibo(5)