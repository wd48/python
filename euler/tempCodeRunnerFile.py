# 소수를 담을 list 선언
a = []
# 200만 이하의 소수판별 이중 for문 
for i in range(2000001):
    result = True
    # 소수 : 1을 제외하므로 False
    if(i<2):
        result = False
    # 
    for j in range(2, i):
        if i%j == 0:
            result = False
    if result:
        a.append(i)

print(sum(a))