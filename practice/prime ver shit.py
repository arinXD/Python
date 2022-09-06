while True:
    a = input("enter number. : ")

    if a=='n':
        break
    a = int(a)
    if a==0:
        print("0 is neither prime or composite")
    
    elif a==1 :
        print("1 is neither prime or composite")
        
    elif a==2 or a==3 or a==5:
        print("prime number")

    elif a%5==0:
        print("composite number")

    elif a%2==1 :
        if a%3==1 or a%3==2:
            print("prime number")
        elif a%3==0 :
            print("composite number")
    else:
        print("composite number")

