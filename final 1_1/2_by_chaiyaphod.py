text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
file = open("input02.txt","r")
write_list = []

def split(x):
    a,b = x.split()
    return a,b

def write(x):
    with open('output02.txt','w+') as w:
        w.writelines(x)
    return;

for line in file:
    list_ans = []
    line = line.strip()
    code,number = split(line)
    #print(code,number)
    number = int(number)
    code = list(code)

    for i in code[number-1::number]:
        result = text.index(i)
        list_ans.append(text[result-3])
        
    #print('= '+''.join(list_ans)+'\n')
    print(''.join(list_ans))
    write_list.append(''.join(list_ans)+'\n')
        
file.close()

write(write_list)
    
