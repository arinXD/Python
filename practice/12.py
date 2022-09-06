input_1 = input("Do you want to start ?(s for start / x for exit)\ninput:")
while True:
    if input_1=="s" or input_1=="S":
        u=input("enter number:")
        while True:
            a = int(u)
            if a>100 or a<0:
                print("error")
            elif a<=100 and a>80:
                print("A")
            elif a<=79 and a>70:
                print("B")
            elif a<=69 and a>=60:
                print("C")
            elif a<=59 and a>=50:
                print("D")
            else:
                print("F")
            u=input("enter number:")
            if u=="n" or u=="N":
                break

    elif input_1=="x" or input_1=="X":
        break

    else:
        print("type only s or x")
    
    input_1 = input("Do you want to start ?(s for start / x for exit)\ninput:")
