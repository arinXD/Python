def check(x,output):
    for name,item in data_item.items():
        check = []
        for i in item:
            if i in x:
                check.append(i)
        if check != []:
            print(name+':',', '.join(check))
            output.append(name+' = '+', '.join(check)+'\n')
    return;

def split(obj):
    for member in obj:
        item, weight = member.split(':')
        u_weight.append(int(weight))
        u_item.append(item)
    return;

u_name = []
u_limit = []
data_item = {}
data_weight = {}

with open('input03.txt','r+')as db:
    for i in db:
        
        u_weight = []
        u_item = []
        
        i = i.strip()
        name, limit, item1, item2 = i.split('|')
        u_name.append(name)
        u_limit.append(int(limit))

        item1 = item1.split(',')
        split(item1)#แยก item, weight ใน def
        item2 = item2.split(',')
        split(item2)
            
        u_weight = sum(u_weight)
        data_item[name] = u_item
        data_weight[name] = u_weight
        
data_limit = dict(zip(u_name,u_limit))

w = ['cola', 'juice', 'wine']
e = ['phone', 'laptop', 'tablet']

out1 = []
out2 = []
out3 = []

print('=== Over weight ===')
for name,limit in data_limit.items():   
    if data_weight[name]>data_limit[name]:
        print(name+'(Weight > {})'.format(data_limit[name]))
        print("{}'s item: ".format(name),', '.join(data_item[name])+'\n')
        out1.append(name+' = '+', '.join(data_item[name])+'\n')

print('\n=== Liquid ===')
check(w,out2)

print('\n=== Electronic ===')
check(e,out3)

with open('output03.2.txt','w+') as dw:
    dw.write('=== {} ==='.format("Overload")+'\n')
    dw.writelines(out1)
    dw.write('\n'+'=== {} ==='.format("Liquid")+'\n')
    dw.writelines(out2)
    dw.write('\n'+'=== {} ==='.format("Electric")+'\n')
    dw.writelines(out3)
