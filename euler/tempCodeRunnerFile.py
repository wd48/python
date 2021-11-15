def factorial(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

a,b = map(int, input('가로세로 몇?').split())

print(int(factorial(a+b)/(factorial(a)*factorial(b))))