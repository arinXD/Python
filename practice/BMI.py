count1=0
count2=0
while True:
    weight = int(input('Weight: '))
    height = int(input('Height: '))
    if weight == 0 or height==0:
        break
    w = weight
    h = height/100
    bmi = w/(h)**2
    if bmi<18.5:
        count1+=1
    if bmi>24.9:
        count2+=1
print('Underweight:',str(count1)+'\n'+'Overweight:',count2)
     

