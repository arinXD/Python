rule = (0,1,2,3,4,5,6,7,8,9)
List = list()

while(True):
    number = int(input("-> "))
    if (number not in rule):
        break
    List.append(number)

#print(List)

for i in range (0,10):
    print("{} = {}".format(i,List.count(i)))

