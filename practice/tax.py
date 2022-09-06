person_1 =int(input("Please Enter revenue :"))
person_2 =int(input("Please Enter revenue :"))
person_3 =int(input("Please Enter revenue :"))
person_4 =int(input("Please Enter revenue :"))
total = person_1+person_2+person_3+person_4

if total<=100000 :
    print("Tax = 0",)
    
elif total>=100001 and total<=500000 :
    print("Tax =",total*0.05)
    
elif total>=500001 and total<=1000000 :
    print("Tax =",total*0.1)
     
else:
    print("Tax =",total*0.2)
