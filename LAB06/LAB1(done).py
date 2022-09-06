minA = 0
maxA = 0
ave = 0
n=0
count1 = 0
while True:
    inputA = int(input("number: "))
    if inputA==0:
        break
    
    ave = ave+inputA
    n = n+1
    
    if count1==0:
        minA = inputA
        maxA = inputA
        count1+=1
    
    elif inputA < minA :
        minA = inputA
        
    elif inputA > maxA :
        maxA = inputA

print("MIN =",minA)      
print('MAX =',maxA)
print('Average =','%.2f'%(ave/n))
    
