# 오일러 24번
'''
순열(permutation)은 어떤 대상을 순서대로 배치한 것을 말한다.
예를 들어 3124는 숫자 1,2,3,4로 만들 수 있는 순열 중 하나다.

모든 순열을 숫자 순이나 사전 순으로 나열할 때는 사전식 순서라고 부른다.
0,1,2의 사전식 순열은 다음과 같다

012 021 102 120 201 210

숫자 0,1,2,3,4,5,6,7,8,9로 만든 순열 중에서 1,000,000번째 순열은 무엇인가?
'''

# permutations 함수를 이용하여 풀기

from itertools import permutations


def Q24_v1(iters, n):
    """iters로 만드는 순열에서 n번째 순열을 찾는다"""
    for i, term in enumerate(permutations(iters), 1):
        if i == n:
            return ''.join(term)


if __name__ == "__main__":
    print("01234의 사전식 순열")
    print("="*20)
    for i in range(10):
        print(f"{i+1:2}번째 순열: {Q24_v1('01234', i+1)}")
