def pack_item(itemsDict,list):
    for name,item in itemsDict.items():
        result=str(name+"("+", ".join(item)+")")
        list.append(result)
def check_item(checkList,addList,item):
    if item in checkList:
        addList.append(item)
        
person=[]
overweight=[]
liquid=[]
electronic=[]
has_water={}
has_elec={}
person_items={}
water=['cola', 'juice', 'wine']
elec=['phone', 'laptop', 'tablet']

with open('input.txt') as file:
    for i in file:
        element=[]
        i=i.strip('\n').split('|')
        element.append(int(i[1]))
        element.append(i[2])
        element.append(i[3])
        person.append({i[0]:element})

for element in person:
    for k,v in element.items():
        #print(k,"=>",v)
        item_list=[]
        limit = v[0]
        weight=0
        items1 = v[1].split(",")
        items2 = v[2].split(",")
        for item in items1:
            item=item.split(":")
            weight+=int(item[1])
            item_list.append(item[0])
        for item in items2:
            item=item.split(":")
            weight+=int(item[1])
            item_list.append(item[0])
        if weight>limit:
            overweight.append(k)
        person_items[k]=item_list
        
for k,v in person_items.items():
    person_has_water=[]
    person_has_elec=[]
    for i in v:
        check_item(water,person_has_water,i)
        check_item(elec,person_has_elec,i)
    if len(person_has_water)>0:
        has_water[k]=person_has_water
    if len(person_has_elec)>0:
        has_elec[k]=person_has_elec
        
pack_item(has_water,liquid)
pack_item(has_elec,electronic)
    
print("Over weight =",", ".join(overweight))
print("Liquid ="," | ".join(liquid))
print("Electronic ="," | ".join(electronic))

with open('output.txt','w') as file:
    file.write("Over weight = "+", ".join(overweight))
    file.write("\nLiquid = "+" | ".join(liquid))
    file.write("\nElectronic = "+" | ".join(electronic))
