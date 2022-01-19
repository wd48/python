## 오일러 프로젝트 #4
# 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
# 두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
# 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까?

# 팰린드롬 수
# 좌우 대칭의 숫자나 문자

# 팰린드롬 확인
# if string == string[::-1]

# 문자열 slice 기능: 끝에 -1 > 거꾸로 뒤집혀서 출력

# 루프문 구성
# for i in range(900,1000):
#     for j in range(900,1000):
#         print(i*j, end=',')

# 루프문 2개 겹쳐서 곱셈
# 가장 큰값을 찾음 > 세자리수 중 900번대 에서부터 시작

# 1. 함수로 분리
def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False

maxValue = 0
for i in range(900,1000):
    for j in range(900,1000):
        product = i*j
        if isPalindrome(str(product)):
            if product > maxValue:
                maxValue = product

print("1번:",maxValue)

# 2. 함수 없이
maxV2 = 0
for i in range(900,1000):
    for j in range(900,1000):
        product = i*j
        if str(product) == str(product)[::-1]:
            if product > maxV2:
                maxV2 = product
print("2번:",maxV2)

# 3. 결과 리스트 저장
result = []
for i in range(900,1000):
    for j in range(900,1000):
        product = i*j
        if str(product) == str(product)[::-1]:
            result.append(product)
print("3번:",max(result))