b = 0
member = list()
memberStr = str()
avg = int()

while True:
    num = input(": ")
    if num.isdigit()==False:
        break

    num=int(num)
    member.append(num)
    
    if (b!=0):
        if num>max:
            max=num
            b += 1
            avg += num
        elif num<min:
            min=num
            b += 1
            avg += num
        else:
            b += 1
            avg += num
        print("Max =",max,", Min =",min,", c =",b,", AVG",avg)
        
    else:
        min, max = num, num
        b += 1
        avg += num
        print("Max =",max,", Min =",min,", c =",b,", AVG",avg)
        
member.sort()

for i in range (0,len(member)):
    if i!=len(member)-1:
        memberStr += str(member[i])+", "
    else:
        memberStr += str(member[i])

print("\nMember =",member)
print("\nMember =",memberStr)
print("Average =",avg/len(member),"\nMax =",max,"\nMin =",min)
