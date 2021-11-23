# 16번, 제곱수 각자리의 합

num_string = str(2**1000)

i = 0
total = 0

for i in num_string:
    total = total + int(i)
print(total)