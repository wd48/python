def collatz(n):
    print("while문 바깥 ",n)
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        print("else 아래 ",n)
    return
print(collatz(13))