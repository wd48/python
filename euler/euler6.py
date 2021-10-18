# 6번 문제

multipleSum = 0
sumMultiple = 0

for i in range(1,101):
    multipleSum += i
    sumMultiple = sumMultiple + (i*i)

multipleSum = multipleSum*multipleSum
print(multipleSum - sumMultiple)