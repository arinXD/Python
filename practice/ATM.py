m1000=0
m500=0
m100=0
sum=0
input_count=0
while True:
    if m1000+m500+m100>20:
            print('Error')
            break

    if input_count==2:
        print('1000 = '+str(m1000)+'\n'+'500 = '+str(m500)+'\n'+
      '100 = '+str(m100))
        break
    in1 = int(input('จำนวนเงิน: '))

    if in1==0:
        print('1000 = '+str(m1000)+'\n'+'500 = '+str(m500)+'\n'+
      '100 = '+str(m100))
        break

    if in1<=20000:
        sum+=in1
        if sum%1000 and sum%500 and sum%100!=0:
            print('Error')
            break
    
        while sum>=1000:
            sum-=1000
            m1000+=1
        while sum>=500:
            sum-=500
            m500+=1
        while sum>=100:
            sum-=100
            m100+=1
        input_count+=1
        
        
    else:
        print('Error')
        break

      
