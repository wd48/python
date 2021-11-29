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