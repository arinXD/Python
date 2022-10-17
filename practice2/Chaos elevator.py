from random import randint

elevator = list()
result = list()
minNumber = int()

for i in range(0,5):
    member = randint(1, 25)
    if(i==0):
        elevator.append(member);
    else:
        if (member in elevator):
            member = randint(1, 25)
            elevator.append(member)
        else:
            elevator.append(member)


floor = int(input("Floor: "))
for i in range(0,5):
    number = elevator[i]-floor
    if(number<0):
        number = number + -(number*2) 
    result.append(number)
print(elevator)
print(result)
minNumber = min(result)
print("Elevator",result.index(minNumber)+1,"is coming")

    
