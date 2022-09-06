result = 0  
n = 0
total_n = 0 
count = 0
while True:
    credit = input('credit: ')
    if credit=='0':
        break
    grade = input('grade: ')
    result += float(credit)*float(grade)
    if count==0:
        n = credit
        credit = 0 
        count += 1
    total_n += float(n)+float(credit)
    n = 0

print('GPA =','%.2f'%float(result/total_n))
#print(result)
#print(total_n)

