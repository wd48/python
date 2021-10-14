# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

# LCM : 최소공배수
# GCD : 최대공약수

# 1. math 이용
import math

LCM = 1

for i in range(1, 21):
    GCD = math.gcd(i, LCM)
    LCM = int(i * LCM/GCD)
    print(i, LCM)

