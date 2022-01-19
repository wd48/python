# 9번 문제

# 세 자연수 a, b, c 가 피타고라스 정리 a2 + b2 = c2 를 만족하면 피타고라스 수라고 부릅니다 
# (여기서 a < b < c ).
# a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까?

# Special Pythagorean triplet

# 1. c항을 연립방정식으로 a^2 + b^2 = (1000-a-b)^2

# 2. 루프문 생성

for x in range(1,1000):
    for y in range(1,x):
        if x**2 + y**2 == (1000-x-y)**2:
            print(x, y, 1000-x-y)
            print(x*y*(1000-x-y))
            break



# ref. 1
for a in range (1,333):
    for b in range(a+1, round((1000-a)/2)):
        if a**2 + b**2 == (1000-a-b)**2:
            print(a)
            print(b)
            print(1000-a-b)
            print(a*b*(1000-a-b))

# ref. 2
for x in range(10,1000):
    for y in range(10,1000):
        z = 1000-x-y
        if x**2 + y**2 == z**2:
            print(x, y, z)
            print(x*y*z)

# ref. 3
for x in range(1,500):
    for y in range(2, 500):
        z = x**2 + y**2
        if x+y+z**(1/2) == 1000:
            print(x*y*z**(1/2))

# ref. 4
def is_pythaforean_triple(a,b,c):
    return c > b > a and a**2+b**2 == c**2

def problem9():
    for i in range(1, 1000):
        for j in range(i+1, 1000):
            for k in range(j+1, 1000):
                if i+j+k == 1000 and is_pythaforean_triple(i,j,k):
                    print(i,j,k)
                    print(i*j*k)
                    return i,j,k

a,b,c = problem9()
print("problem9 def is... ",a*b*c)