# 오일러 21번
# 10000 이하 모든 친화수(우애수)의 합
'''
 d(n)을 d의 진약수를 모두 더한 값이라고 정의하자.
 (진약수 : n보다 작은 약수)
 만약 a != b 일 때, d(a)=b 이고 d(b)=a 이면, a와 b를 친화수(amicable numbers) 라고 한다

진약수 구하기
  예를 들어 16의 진약수는 1x16, 2x8, 4x4에서 16을 제외한 1,2,4,8이다.
  * 1은 모든 수의 약수, 정답 리스트를 [1]로 초기화한다.
  * 2부터 주어진 수의 제곱근까지 반복한다.
    - 주어진 수가 제수로 나누어 떨어지면 리스트 answer에 제수와 몫을 추가한다
  * 4x4 와 같은 경우에 같은 값이 두 번 들어가지 않도록 처리한다

  중복을 허용하지 않는 집합(set)을 이용하자. 리스트(list)를 사용하면 고려할 점이 더 있는데,
  이것은 직접 구현해보자
'''

def proper_divisors(n):
    """자연수 n의 진약수를 구하여 집합으로 반환한다."""
    answer = {1}
    for div in range(2, int(n**0.5) + 1):
        q, r = divmod(n, div)
        # not r : r이 0인 경우
        if not r:
            answer.update([q, div])
    return answer

if __name__ == "__main__":
    print(f"220의 진약수: {sorted(proper_divisors(220))}")
    print(f"16의 진약수: {sorted(proper_divisors(16))}")


'''
친화수 확인하기
  * 먼저 주어진 수(n)의 진약수의 합(m)을 구한다.
  proper_divisors 함수에서 받은 값을 sum()으로 더한다.
  * 진약수의 합(m)을 다시 proper_divisors 함수에 넣어 구한 값이 주어진 수(n)와 같으면 친화수이다.
'''
def is_amicable(n):
    """n이 친화수이면 true, 아니면 false를 반환한다."""
    m = sum(proper_divisors(n))
    return True if n == sum(proper_divisors(m)) else False

if __name__ == "__main__":
    print(f"is 220 amicable number? -> {is_amicable(220)}")
    print(f"is 284 amicable number? -> {is_amicable(284)}")

'''
반복문으로 풀기
>> 문제를 해결하려면 10,000까지 계산을 반복하는데, 그 안에는 진약수를 구하기 위해 for문을 또 돌린다.
계산 횟수를 줄일 방법을 생각해 보자.
  * 조건에서 친화수 a와 b는 다른 값이므로 a>b 또는 b>a 라는 의미다. 이걸 이용하자
  * 작은 수부터 검사하므로, 이 수를 a라고 하면 친화수의 쌍인 b는 a보다 커야 한다.
  * 즉, b>a 일 때만 친화수인지 계산하다. 그리고 b는 10,000 미만이어야 한다.
  * is_amicable 함수의 코드를 solution 함수에 넣자
'''

def Q21_v21(n):
    """n 미만의 친화수를 모두 구하여 더한다."""
    answer = 0
    for a in range(2, n):
        b = sum(proper_divisors(a))
        if (n > b > a) and a == sum(proper_divisors(b)):
            answer += (a+b)
    return answer

if __name__ == "__main__":
    print(Q21_v21(300))