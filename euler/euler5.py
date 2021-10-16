# 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
# 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

# LCM : 최소공배수
# GCD : 최대공약수

# 1. math 이용
# import math

# LCM = 1

# for i in range(1, 21):
#     GCD = math.gcd(i, LCM)
#     LCM = int(i * LCM/GCD)
#     print(i, LCM)

# 2
# n=1부터 시작해서 1~20 사이의 수를 나눠서 0을 만족하는 수를 나오게 함

n = 1

# a : 1부터 20까지의 수를 나눠서 나눈 나머지가 0인 c를 담는다
# b :
a = list()
b = list()

while True:
    print(n)
    for i in range(1,21):
        c = n%i 
        # c: n을 1~20까지 반복하면서 나눈 나머지를 본다
        zero = 0
        a.append(c)
        b.append(zero)
    
    if (a==b) == True:
        print("answer: ",n)
        break
    a.clear()
    b.clear()
    n += 1