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