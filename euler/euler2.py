# 피보나치 수열에서 짝수이면서 4백만 이하인 값을 모두 더하기

# n1 = 0
# n2 = 1
# n3 = n1+n2
# result = 0

# while n3 <= 4000000:
#     n3 = n1+n2
#     n1 = n2
#     n2 = n3

#     if n3 % 2==0:
#         result += n3

# print(result)

# 2
# class Fibonacci:
#     # 초기화
#     def __init__(self):
#         self.a = 0
#         self.b = 1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         c = self.a + self.b
#         if self.a > self.b:
#             self.b = c
#         else:
#             self.a = c
#         return c

# if __name__ == '__main__':
#     s = 0
#     fibonacci = Fibonacci()
#     for n in fibonacci:
#         if n >= 4000000:
#             break
#         else:
#             if n % 2 == 0:
#                 s += n
#     print(s)

# 3
# fibo_odd_sum : 짝수일 때 합
fibo_odd_sum = 2

fibo1 = 1
fibo2 = 2
fibo3 = 0

while(True):
    # fibo3 = 총합이 400만 될때까지 수행
    if(fibo3 > 4000000):
        break
    # 피보나치 수열: (n+2)=(n)+(n+1) 
    fibo3 = fibo1 + fibo2
    print("fibo3 = ", fibo3)

    # 짝수일 때 짝수에 해당하는 n+2 항의 값을 더해줌
    if(fibo3 % 2 == 0):
        fibo_odd_sum += fibo3
        print("fibo_odd_sum = ", fibo_odd_sum)
    
    # 피보나치 수열 적용 : while문 반복시 n, n+1을 피보나치 수열 규칙으로 적용되도록 해야함
    fibo1 = fibo2
    fibo2 = fibo3

    print("n = ",fibo1)
    print("n+1 = ",fibo2)

print("fibo_odd_sum = ", fibo_odd_sum)