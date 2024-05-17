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
    print("0123456789의 사전식 순열")
    print("="*20)
    for i in range(1000):
        print(f"{i+1:2}번째 순열: {Q24_v1('0123456789', i+1)}")


# https://opentutorials.org/module/3075/18309
# 함수부분
'''
순열의 패턴을 보면
0123456789 : 제일 작은 수, 다음수는 맨 오른쪽의 8과 9를 교환
0123456798 : 98은 최대값이므로 앞의 7과 8을 교환하고 7과 9는 최소가 되도록 79로 정렬
0123456879 : 맨 오른쪽 끝의 7과 9를 교환
0123456897 : 97은 최대로 올라가있으므로 왼쪽 8을 9와 교환한 후 7과 8은 최소가 되도록 78로 정렬
0123456978
0123456987

마지막숫자 다음에 올 숫자는 0123457689
- 위 마지막 숫자에서 끝의 세자리 987은 이미 최대로 자리가 올라가 있으므로, 그 앞에 있는 6이 숫자가 올라가야 되고,
새로운 수는 오른쪽에 있는 수 중에서 그 다음으로 큰 수인 7이다
(오른쪾에 7이 없으면 8이나 9가 될 수도 있다)
- 7을 6의 자리에 넣고, 남은 698을 오름차순으로 정렬해서 689를 만들어 뒷부분에 붙인다
'''


def get_next_permutation(string):
    i = len(string)-2  # i=8
    while i >= 0:
        # string[8] < string[9]? => true
        if string[i] < string[i+1]:
            # target = sorted(string[8:])
            target = sorted(string[i:])
            print('target : ', target)
            new_num = target.pop(target.index(string[i])+1)
            print('new_num : ', new_num)
            last_nums = ''.join(target)
            print('last_nums : ', last_nums)
            return string[:i] + new_num + last_nums
        i -= 1


string = '0123456789'

# 루프문 만들기
# 첫번째 수인 0123456789 부터 백만까지 루프문을 만든다
# range에는 100만이 포함이 안되서 실제로는 999999개 이지만 시작하는 숫자가 첫번째이기 때문에 100만번째 수
for i in range(1, 10):
    string = get_next_permutation(string)
print(string)
