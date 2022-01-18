# 팩토리얼 자릿수의 합

# 팩토리얼 계산

def fact(num):
    total=1
    while num>0:
        total*=num
        num-=1
    return total

print(fact(10))

# from math import factorial
# factorial(10)

# 자릿수 합

print("===========")

def fact(num):
    total=1
    for i in range(1, num+1):
        total*=i
    return total
# 결과값을 담음
result=fact(10)
# string으로 str 사용해서 다 쪼갬
string=str(result)
print(string)

total = 0

for i in string:
    total += int(i)

print(total)

# 100! 계산

def fact(num):
    total=1
    for i in range(1,num+1):
        total*=i
    return total

result = fact(100)
print(result)

string=str(result)

total = 0

for i in string:
    total+=int(i)
print(total)