# 16번, 제곱수 각자리의 합

num_string = str(2**1000)

i = 0
total = 0

for i in num_string:
    total = total + int(i)
print(total)

# ref1.
result = list(str(2**1000))
sum = 0
for i in result:
    sum += int(i)

print(sum)

# ref2.
number = 2**1000
total = 0

number_list = list(str(number))
print(number_list)

for i in range(len(number_list)):
    total += int(number_list[i])

print(total)