# 15번
# 가로세로 20 격자 길에서 왼쪽 위 모서리에서 오른쪽 아래 모서리로 가는 경우의 수

#팩토리얼
def factorial(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

a,b = map(int, input('가로세로 몇?').split())

print(int(factorial(a+b)/(factorial(a)*factorial(b))))

# 오른쪽으로 가는 수 p, 아래로 가는 수 q
# (p+q)! / (p!)*(q!)