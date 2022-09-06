list_0 = []

def check(x):
    x = x.replace(' ','')
    return x

with open('input01.txt','r') as db:
    for line in db:
        line = line.strip()
        find = line.find(' ')
        if find >=0:
            new_line = check(line)
        else:
            new_line = line
            
        i = new_line[::-1]
         
        if new_line == i:
            print(line+'\t1')
            list_0.append(line+'\t1\n')
        else:
            print(line+'\t0')
            list_0.append(line+'\t0\n')
with open('output01_026.txt','w+') as dw:
    dw.writelines(list_0)
