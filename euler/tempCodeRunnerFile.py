import time
start_time = time.time()

def collatz(n):
    count=1
    while n != 1:
        # 수열만들면서 저장값 확인
        if (n) in cache :
            # 저장값이 있으면 저장된 값으로 대체
            count += cache[n]-1
            n = 1
        else :
            if n%2 == 0:
                n=n/2
            else:
                n=n*3+1
            count+=1
    return count

cache={}
i=1;maxVal=0

while i<1000000:
    val = collatz(i)
    if val > maxVal :
        maxVal = val
    cache[i] = val
    i+=1
    print(collatz(i))

print(maxVal)
print(val)
print("calculation time: ", time.time()-start_time)