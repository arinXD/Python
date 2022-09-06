count_a = 0
count_b = 0
count_other = 0
while True:
    character=input('อักขระ: ')
    if character=='y' or character=='Y':
        print('A = '+str(count_a)+'\n'+'B = '+str(count_b)+'\n'+'other charactor =',count_other)
        break
    elif character=='a' or character=='A':
        count_a += 1
    elif character=='b' or character=='B':
        count_b += 1
    else:
        count_other += 1
        
    
