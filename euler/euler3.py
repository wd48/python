# 소인수분해

# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

# 600851475143 의 소인수 중에서 가장 큰 수를 구하세요.

# 소수 : 양의 약수를 2개만 가지는 자연수

# 1 소인수분해를 한다
# (나눠지는 수) / (나누는 수) = (몫) + (나머지)
target = 600851475143
i = 2
# 1-1 나누는 몫을 리스트에 담아서 비교하자
target_list = []

# while 참일 때 : break할 때까지 수행
while target > 1:
    # 소인수 분해가 된다 > 나누는 수 +1
    if target % i == 0:
        # target을 i로 나눈 수로 대체 : 계속 나누게 함
        target /= i
        target_list.append(i)
    # 나눠지는 수가 1이 된다 => 소인수분해가 완료되었다 = while문 종료
    elif target == 1:
        break
    else:
        i += 1

print(target_list)
print(max(target_list))

# 2
# a : 처음 숫자, b : 마지막 숫자
a = 1
b = 600851475143
# a가 b가 되면 끝 = b가 다 나눠져서 그 값이 1이 되면 끝
while a<b:
    if b % a == 0:
        b = b/a
        print(b)
    a += 1
        