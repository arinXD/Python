def missing_number(number):
    number = sorted(number)
    missing = []
    new_missing=''
    for i in range(number[0],number[-1]+1,):
        if i not in number:
            missing.append(str(i))
    index=len(missing)
    for i in range(0,index):
        if i!=index-1:
            new_missing+=missing[i]+', '
        else:
            new_missing+=missing[i]
    print('Lost numbers contain:',new_missing)
    return;
    
num = [10, 11, 15, 12, 9, 14, 7]
#num = [12, 5, 9, -3]
missing_number(num)
