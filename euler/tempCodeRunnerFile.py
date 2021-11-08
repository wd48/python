def collatz(n):
    count=1
    while not n==1:
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
        count+=1
    return count

i=1;maxVal=0

while i<100:
    val = collatz(i)
    if val>maxVal :
        maxVal = val
        print(i, maxVal)
    i+=1