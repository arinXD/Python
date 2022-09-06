dict1 = {}
dict2 = {}
water = ['cola', 'juice', 'wine']
elec = ['phone', 'laptop', 'tablet']
overload = ['Overload:']
liquid = {}
electronic = {}

def check_water(x):
    c = 0
    for i in x:
        if i in water:
            c+=1
        else:
            pass
    if c>0:
        
        return '- พบของเหลว'
    
    else:
        return '- ไม่พบของเหลว'
    
def check_elec(y):
    c2 = 0
    for i in y:
        if i in elec:
            c2+=1
        else:
            pass
    if c2>0:
        
        return '- พบอุปกรณ์อิเล็กทรอนิกส์'
    
    else:
        return '- ไม่พบอุปกรณ์อิเล็กทรอนิกส์'

with open('input03.txt','r') as db:
    for i in db:
        list1 = []
        list2 = []
        i = i.strip()
        name,total,kg1,kg2 = i.split('|')
        kg1 = kg1.split(',')
        kg2 = kg2.split(',')

        for i in kg1:
            n,p = i.split(':')
            list1.append(int(p))
            list2.append(n)
        for j in kg2:
            n,p = j.split(':')
            list1.append(int(p))
            list2.append(n)

        dict1[name] = {int(total):list1}
        dict2[name] = list2

for key1,value1 in dict1.items():
    list_elec = []
    list_liquid = []
    for k1,y1 in value1.items():
        if sum(y1)>k1:
            print('='*15)
            print(key1,'รวม',sum(y1),'KG')
            print('- เกิน',k1,'KG')
            print('- สัมภาระ:',','.join(dict2[key1]))
            print(check_water(dict2[key1]))
            for i in dict2[key1]:
                if i in water:
                    print(' คือ '+i)
                    list_liquid.append(i)
                    liquid[key1] = list_liquid

            print(check_elec(dict2[key1]))
            for i in dict2[key1]:
                if i in elec:
                    print(' คือ '+i)
                    list_elec.append(i)
                    electronic[key1] = list_elec
            print('')
            #overload.append(key1+' = '+','.join(dict2[key1])+' |')
            overload.append(key1)
            
                
        else:
            print('='*15)
            print(key1,'รวม',sum(y1),'KG')
            print('- ไม่เกิน',k1,'KG')
            print('- สัมภาระ:',','.join(dict2[key1]))
            print(check_water(dict2[key1]))
            for i in dict2[key1]:
                if i in water:
                    print(' คือ '+i)
                    list_liquid.append(i)
                    liquid[key1] = list_liquid
            print(check_elec(dict2[key1]))
            for i in dict2[key1]:
                if i in elec:
                    print(' คือ '+i)
                    list_elec.append(i)
                    electronic[key1] = list_elec
            
            print('')
            

new_list = []
new_list2 = ['Liquid: ']
new_list3 = ['Electronic: ']

for i in overload:
    new_list.append(i+' ')
    
for key , value in liquid.items():
    new_list2.append(key+' = '+', '.join(value)+'|')
    
for key , value in electronic.items():
    new_list3.append(key+' = '+', '.join(value)+'|')

'''print(new_list)
print(new_list2)
print(new_list3)'''

with open('output03_026.txt','w+') as dw:
    dw.writelines(new_list)
    dw.write('\n')
    dw.writelines(new_list2)
    dw.write('\n')
    dw.writelines(new_list3)
