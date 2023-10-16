# 오일러 22번
# q022_names.txt : 5천개 이상의 영문 이름들이 들어있는 텍스트 파일의 각 이름에 대해 점수를 매긴다
# 먼저 모든 이름을 알파벳 순으로 정렬한다
# 각 이름에 대해서, 그 이름을 이루는 알파벳에 해당하는 수 (A=1, B=2, ...)를 모두 더한다
# 여기에 이 이름의 순번을 곱한다

'''
문제 분석, 함수 생성
1) 파일을 읽어와서 이름을 정렬한다
2) 이름의 총 개수, COLIN의 위치 확인하기

- 파일 불러올 때 , 기준으로 이름을 분리, 리스트에 저장
- strip() 이용하여 큰따옴표 제거
- 알파벳 순으로 정렬
'''
import sys
with open("q022_names.txt", "r") as f:
    names = [name.strip('"') for name in f.read().split(",")]
names.sort()

if __name__ == "__main__":
    print("이름 총 개수 : ", len(names))
    print("COLIN 위치 : ", names.index("COLIN"))

'''
파일을 처리하고 이름을 정렬하는 코드를 함수에 넣고, 아래 흐름대로 해결한다
1) enumerate를 이용하여 이름과 정렬된 이름의 위치를 하나씩 가져온다.
- 이 때 enumerate의 두 번째 인자에 1을 넣어서 시작 인덱스를 1로 설정한다 (초기화)
2) 문자열에서 글자를 하나씩 가져와서 ord()로 이름값을 구한다
3) 이름값과 이름의 위치를 곱한다.
'''


def Q22_v1(file_name):
    """파일에 있는 이름값을 구하고, 모든 이름값을 더한다."""
    with open(file_name, "r") as f:
        names = [name.strip('"') for name in f.read().split(",")]
    names.sort()

    answer = 0
    base = ord("A") - 1  # 알파벳순으로 1,2,..의 값을 주기위한 기준점

    for pos, name in enumerate(names, 1):
        name_val = 0
        for ch in name:
            name_val += ord(ch) - base
        answer += name_val * pos
    return answer


if __name__ == "__main__":
    print(Q22_v1("q022_names.txt"))
