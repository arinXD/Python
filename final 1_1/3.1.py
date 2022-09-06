def split(x):
    for i in x:
        i = i.split(':')
        list_item.append(i[0])
        list_total.append(int(i[1]))
    return

dict_limit = {}
dict_total = {}
dict_item = {}

with open('input03.txt','r') as db:
    for line in db:
        
        list_total = []
        list_item = []
        
        line = line.strip()
        name,limit,pocket,backpack = line.split('|')
        
        pocket = pocket.split(',')
        backpack = backpack.split(',')
        split(pocket)
        split(backpack)

        dict_limit[name] = int(limit)
        dict_total[name] = sum(list_total)
        dict_item[name] = list_item

n = []
l = []
t = []
water = ['cola', 'juice', 'wine']
elec = ['phone', 'laptop', 'tablet']
write_overload = []
write_liquid = []
write_electronic = []

for name_limit,limit in dict_limit.items():
    n.append(name_limit)
    l.append(limit)
for total in dict_total.values():
    t.append(total)
    
'''print('Name:',n)
print('Limit:',l)
print('Total:',t)'''

print('='*5+' Overload '+'='*5)
for i in range(0,len(n)):
    if t[i] > l[i]:
        print(n[i],':',', '.join(dict_item[n[i]]))
        write_overload.append(n[i]+' : '+', '.join(dict_item[n[i]])+'\n')
    else:
        pass

    
print('\n'+'='*5+' Liquid '+'='*5)
for name,item in dict_item.items():
    show_liquid = []
    for i in item:
        if i in water:
            show_liquid.append(i)
    if show_liquid != []:
        print(name,':',','.join(show_liquid))
        write_liquid.append(name+' : '+','.join(show_liquid)+'\n')

print('\n'+'='*5+' Electronic '+'='*5)
for name,item in dict_item.items():
    show_elec = []
    for i in item:
        if i in elec:
            show_elec.append(i)
    if show_elec != []:
        print(name,':',','.join(show_elec))
        write_electronic.append(name+' : '+','.join(show_elec)+'\n')


with open('output03.txt','w+')as w:
    w.write('=== Overload ==='+'\n')
    w.writelines(write_overload)
    w.write('\n'+'=== Liquid ==='+'\n')
    w.writelines(write_liquid)
    w.write('\n'+'=== Electronic ==='+'\n')
    w.writelines(write_electronic)
