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
