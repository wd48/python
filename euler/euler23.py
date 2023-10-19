# 오일러 23번
'''
*진약수 : 어떤 자연수를 n이라고 할 때, n의 약수 중 n 자신을 제외한 모든 약수

완전수(perfect number) : 진약수의 합이 자신과 같은 수
    ex) 28 : 1+2+4+7+14=28
진약수의 합이 자신보다 작으면 부족수, 자신보다 크면 과잉수라고 한다
    ex) 12의 진약수의 합은 1+2+3+4+6=16, 가장 작은 과잉수

과잉수(12) 두 개를 더해서 얻을 수 있는 가장 작은 수는 24이다.
수학적 분석에 따르면 28, 123보다 큰 모든 정수는 과잉수 두 개를 더해서 만들 수 있다.

과잉수 두 개의 합으로 나타낼 수 없는 가장 큰 수는 28, 123보다 작고,
분석에 따르면 이 상한선을 더 낮출 수 없다

과잉수 두 개의 합으로 나타낼 수 없는 모든 양수의 합을 구하라
'''

# 문제 분석, Solution 함수 만들기
'''
1) 두 과잉수의 합으로 나타낼 수 없는 양수는 모두 28123 미만이다
2) 28123 미만의 수에서 과잉수 두 개의 합으로 나타낼 수 없는 수의 합을 구하라
> 28123까지의 수 중에서 두 과잉수(abundant)의 합으로 나타낼수 없는 수를 찾는 것이다.
: 범위가 28123인 이유는 수학적으로 28123보다 큰 모든 수는 abundant 한 두 수의 합으로 표현이 가능하다고 함
'''

# 1 완전수 확인하기
# 진약수를 구하는 함수를 이용해서 완전수인지, 부족수나 과잉수인지를 확인하는 함수 만들기


def proper_divisors(n):
    """자연수 n의 진약수를 구하여 집합으로 반환한다."""
    answer = {1}
    for div in range(2, int(n**0.5) + 1):
        q, r = divmod(n, div)
        # not r : r이 0인 경우
        if not r:
            answer.update([q, div])
    return answer


def is_perfect_number(n):
    """n이 완전수이면 0, 부족수이면 -1, 과잉수이면 1 반환"""
    sum_of_divisors = sum(proper_divisors(n))
    if sum_of_divisors > n:
        return 1
    elif sum_of_divisors < n:
        return -1
    else:
        return 0


if __name__ == "__main__":
    for n in (12, 16, 28):
        print(f"{n} -> {is_perfect_number(n)}")


# 2 과잉수 구하기
# 이중 반복문을 사용한다
'''
28123개의 숫자를 하나씩 다 조사해서, 별도의 변수에 저장한다.
6965개의 데이터가 변수 안에 저장되며너 된다.
'''


def get_abundant(n):
    """n 이하의 과잉수를 찾아 리스트로 반환한다."""
    # 12 : 가장 작은 과잉수라 조건으로 사용함
    if n < 12:
        return []

    answer = [12]
    for i in range(13, n+1):
        if sum(proper_divisors(i)) > i:
            answer.append(i)
    return answer


if __name__ == "__main__":
    print(len(get_abundant(28123)))

# 3 기능별로 함수를 분리하기
# - 진약수의 합을 반환하는 함수
# - 과잉수 목록을 반환하는 함수
# - 두 함수를 이용하여 답을 찾는 함수
'''
계산량 줄이기
- 과잉수를 찾기 위해 반복적으로 많은 계산을 실행한다.
여기에 답을 찾기 위해 이중 반복문 안에서 더하기 연산과 비교 연산을 해야 한다.
실제로 6965 * 6965번의 반복문을 돌리면 시간이 너무 걸린다.

1) 1부터 28,123 까지의 합은 간단한 공식으로 구할 수 있다.
이 값에서 두 과잉수의 합으로 나타낼 수 있는 수의 합을 뺀다.
2) 과잉수 6965개를 모두 검사하지 말자.
    2)-1 첫째 반복문에서 어떤 과잉수 n1이라 할 때 n1+n1이 28,123보다 커지면 반복문을 벗어난다.
    2)-2 둘째 반복문에서 두 과잉수 n1,n2의 합을 구할 때(n1+n2) 합이 28,123보다 커지면 반복문을 벗어난다.

*과잉수 : 진약수의 합이 자기 자신보다 큰 수
'''
# 진약수의 합을 반환하는 함수


def sum_of_divisors(n):
    """자연수 n의 진약수의 합을 반환한다."""
    answer = 1
    for div in range(2, int(n ** 0.5) + 1):
        q, r = divmod(n, div)
        if not r:
            answer += (q + div)
    if div * div == n:
        answer -= div
    return answer

# 과잉수 목록 반환 함수 - get_abundant 함수 사용


def Q23_v1(n):
    """n 이하에서 과잉수 두 개의 합으로 나타낼 수 없는 수의 합을 구한다."""
    # 중복을 검사할 집합
    check = set()
    total = n * (n+1) // 2
    sub_total = 0
    abundant = get_abundant(n)

    for i in range(len(abundant)):
        # 첫째 조건 : 과잉수의 합이 28,123보다 크면 계산하지 않는다.
        if abundant[i] * 2 > n:
            break
        for j in range(i, len(abundant)):
            # 둘째 조건 : 두 과잉수의 합이 28,123보다 크면 계산하지 않는다.
            if (res := abundant[i] + abundant[j]) > n:
                break
            elif res not in check:
                sub_total += res
                check.add(res)
    return total - sub_total


if __name__ == "__main__":
    print(Q23_v1(28123))


# simple version

# 1 약수의 합
# 12는 가장 작은 abundant(과잉수)이다.
def divisors(n):
    i = 2
    total = {1}
    loop = n**0.5
    while i <= loop:
        if n % i == 0:
            total.add(i)
            total.add(n/i)
        i += 1
    return sum(total)


# 2 abundant(과잉수) 리스트 만들기
# 28123개의 숫자를 하나씩 다 조사해서, 별도의 변수에다 저장해준다.
# 변수타입은 list를 사용해도 되지만, 이 문제에서는 set이 편하다
abun = set()
for i in range(1, 28124):
    if i < divisors(i):
        abun.add(i)

# 3 메인 루프문
# abundant 리스트를 가지고 2개의 중첩 루프문을 만든다
# abundant(과잉수) 두개의 합 을 만드는 코드
# 이 코드가 28123의 범위 안에 있는지 확인해서, 있으면 미리 만들어 놓은 리스트에서 삭제한다
# 그러고 남는 숫자가 abundant(과잉수) 두 개의 합으로 나타낼 수 없는 숫자이다.
numbers = set(range(28123))
for i in abun:
    for j in abun:
        if (i+j) in numbers:
            numbers.remove(i+j)
print(sum(numbers))
