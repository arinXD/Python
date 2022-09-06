number = int(input('number : '))
count=0
for i in range(1,number+1,1):
    if number%i==0:
        count+= 1
#if count==0:
    #print("0 is neither prime or composite")
#elif count==1:
    #print("1 is neither prime or composite")
if count==2:
    print("prime number")
else:
    print('composite number')
