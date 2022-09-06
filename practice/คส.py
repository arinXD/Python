from datetime import datetime

def AD():
    print('\nAnno Domini')
    print('AD to BE')
    try:
        ad = int(input('=> '))
    except:
        print('\nNone\n')
    else:
        if ad == 0:
            return;
        else:
            print("\nA.D. = "+str(ad))
            print("B.E. = "+str(ad+543))
            print("Years = "+str(now-ad))
            print("-"*15+"\n")    
    return;
    
def BE():
    print('\nBuddhist calendar')
    print('BE to AD')
    try:
        be = int(input('=> '))
    except:
        print('\nNone\n')
    else:
        if be == 0:
            return;
        else:
            print("\nB.E. : "+str(be))
            print("A.D. : "+str(be-543))
            new = now + 543
            print("Years : "+str(new-be))
            print("-"*15+"\n")   
    return;

now = str(datetime.now())
now = int(now[:4])

while True:
    print('A.D.[1]\nB.E.[2]')
    try:
        choose = int(input('=> '))
    except:
        print('\nNumber\n')
    else:
        if choose == 1:
            AD()
        elif choose == 2:
            BE()
        else:
            print('*****')
            pass
