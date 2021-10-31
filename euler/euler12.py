# 12번 문제
# 500개 이상의 약수를 갖는 가장 작은 삼각수는?

# 삼각수 : 1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.

# 약수의 갯수 구하는 함수
# 루프 100까지 돌려 약수 객수를 카운트하는 함수

def count_factors(num):
    loop=num**0.5
    # square number
    if loop==int(loop):
        count=1
    else:
        count=0
    i=1
    while i<loop:
        if num%i==0:
            print(i, end=',')
            count+=2
        i+=1
    print()
    return count

i=1;tri_num=0

while i<100:
    tri_num = tri_num + i
    count = count_factors(tri_num)
    print("loop: ",i,"tri_num: ",tri_num,"count: ",count)
    i += 1
    print()

# 루프 무한, 카운트 500개 넘기면 break
import time
start_time = time.time()

def count_factors(num):
    loop=num**0.5
    # square number
    if loop==int(loop):
        count=1
    else:
        count=0
    i=1
    while i<loop:
        if num%i==0:
            print(i, end=',')
            count+=2
        i+=1
    print()
    return count

i=1;tri_num=0
# 무한루프
while True:
    tri_num = tri_num + i
    count = count_factors(tri_num)
    print("loop: ",i,"tri_num: ",tri_num,"count: ",count)
    if count > 500:
        break
    i += 1

print("answer: ",tri_num)
print("calculation time: ", time.time()-start_time)

# ref.
# 진짜 오래걸림 ㄹㅇ;

x=0;y=0;z=[1];i=1

while max(z)*2 < 500:
    x = x+i
    for j in range(2, int(x**0.5)+1):
        if x%j==0:
            y +=1
        z.append(y)
    print(x, max(z)*2 + 2)
    y = 0
    i += 1