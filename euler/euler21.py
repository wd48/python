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
        if not r:
            answer.update([q, div])
    return answer

if __name__ == "__main__":
    print(f"220의 진약수: {sorted(proper_divisors(220))}")
    print(f"16의 진약수: {sorted(proper_divisors(16))}")


