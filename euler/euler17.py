# 17번
# 숫자를 알파벳으로 변환하고 글자수를 세는 문제

# 1 정석

# 딕셔너리
data1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
data2='''one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety'''
numbers=dict(zip(data1,data2.split()))

# dict() 딕셔너리 타입생성
# zip() 나열형의 자료형 2개를 짝으로 만들어 묶어준다

# total=0
# for i in range(1,21):
    # total += len(numbers[i])
    # print(i, numbers[i], len(numbers[i]), total)

# 100까지 출력
# def func(num):
#     if (num) not in numbers:
#         numbers[num] = numbers[num - num % 10] + numbers[num % 10]
#     return numbers[num]

# total=0
# for i in range(1,100):
#     value=func(i)
#     total += len(value)
#     print(i, value, len(value), total)

# 1000까지 계산

def func(n):
    if n <100:
        if (n) not in numbers:
            numbers[n] = numbers[n - n % 10] + numbers[n % 10]
        return numbers[n]
    if n <1000:
        if n==0:
            return numbers[n//100] + numbers[100]
        return numbers[n//100] +  numbers[100] + 'and' + numbers[n % 100]
    return 'one' + numbers[1000]
 
total = 0
for i in range(1,1001):
    value = func(i)
    total += len(value)
    print(i, value, len(value), total)

# ref.
# https://thisblogbusy.tistory.com/entry/1%EB%B6%80%ED%84%B0-1000%EA%B9%8C%EC%A7%80-%EC%98%81%EC%96%B4%EB%A1%9C-%EC%8D%BC%EC%9D%84-%EB%95%8C-%EC%82%AC%EC%9A%A9%EB%90%9C-%EA%B8%80%EC%9E%90%EC%9D%98-%EA%B0%9C%EC%88%98%EB%8A%94
numbers_string = [None] * 1001 
numbers_string[1] = 'one' 
numbers_string[2] = 'two' 
numbers_string[3] = 'three' 
numbers_string[4] = 'four' 
numbers_string[5] = 'five' 
numbers_string[6] = 'six' 
numbers_string[7] = 'seven' 
numbers_string[8] = 'eight' 
numbers_string[9] = 'nine'
numbers_string[10] = 'ten' 
numbers_string[11] = 'eleven' 
numbers_string[12] = 'twelve' 
numbers_string[13] = 'thirteen' 
numbers_string[14] = 'fourteen' 
numbers_string[15] = 'fifteen' 
numbers_string[16] = 'sixteen' 
numbers_string[17] = 'seventeen' 
numbers_string[18] = 'eighteen' 
numbers_string[19] = 'nineteen' 
numbers_string[20] = 'twenty' 
numbers_string[30] = 'thirty' 
numbers_string[40] = 'forty' 
numbers_string[50] = 'fifty' 
numbers_string[60] = 'sixty' 
numbers_string[70] = 'seventy' 
numbers_string[80] = 'eighty' 
numbers_string[90] = 'ninety' 
numbers_string[100] = 'one hundred' 
numbers_string[200] = 'two hundred' 
numbers_string[300] = 'three hundred' 
numbers_string[400] = 'four hundred' 
numbers_string[500] = 'five hundred' 
numbers_string[600] = 'six hundred' 
numbers_string[700] = 'seven hundred' 
numbers_string[800] = 'eight hundred' 
numbers_string[900] = 'nine hundred' 
numbers_string[1000] = 'one thousand' 

for i in range(20, 100, 10): 
    for j in range(1, 10): 
        idx = i + j 
        numbers_string[idx] = numbers_string[i] + " " + numbers_string[j] 
        
for i in range(1, 10): 
    for j in range(1, 100): 
        idx = (i * 100) + j 
        numbers_string[idx] = numbers_string[i] + " hundred and " + numbers_string[j] 
        
letters_cnt = 0 
for num in numbers_string: 
    if num is None: 
        continue 
    
    letters = num.replace(" ", "") 
    letters = letters.replace("-", "") 
    letters_cnt += len(letters) 
    
print(letters_cnt) # 21124 
# print(numbers_string)

# ref. library num2words
from num2words import num2words

lenth=0
for i in range(1, 1001):
    lenth = lenth + len(((num2words(i)).replace(" ","")).replace("-",""))
print(lenth)


# ref. 
#1~20 -> 각각 대응, 30, 40등은 조합해서 사용
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
            'hundred', 'and', 'thousand']                       #len => 30
sum = 0
index = [0, 0, 0]
string = []
#0~9 합 구하기
sum_10 = 0
for i in range(9):
    sum_10 += len(numbers[i])

for i in range(1000):
    r = i + 1
    #index 정하기
    index = [0, 0, 0]
    #방법2 : str형 이용
    k = str(r)
    for j in range(len(k)):
        index[2-j] = int(k[-(j + 1)])    
    
    #string 초기화
    string = []

    #1000
    if r == 1000:       
        string = numbers[0] + numbers[-1]
                                      
    #100, 200, ..., 900
    elif r % 100 == 0 and r // 100 > 0:
        string = numbers[index[0] - 1] + numbers[27]
    #일반 케이스 - 1~ 19
    elif r % 100 < 20 :
        string = numbers[(r%100) - 1]
        if r > 100 :
            string = numbers[index[0] - 1] + numbers[27] + numbers[28] + string
    #일반 케이스 - 20 ~ 99
    else:
        string = numbers[index[1] + 17]     #십의자리
        if r % 10 != 0 :
            string = string + numbers[index[2] - 1]     #일의자리 
        if r > 100 :
            string = numbers[index[0] - 1] + numbers[27] + numbers[28] + string

    sum += len(string)
print('sum :', sum)