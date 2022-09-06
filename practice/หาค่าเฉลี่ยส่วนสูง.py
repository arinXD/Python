count = 0
high=0   
while True:
    a = float(input("heigh="))
    
    high += a
    count+=1
    if a==99:
        break
print('%.2f'%(high/count))
    
