file = 'student.txt'
ID_list = list()
name_list = list()
dict_score = dict()
first_line = 0

try:
    with open(file,'r') as db:
        for line in db:
            try:
                if first_line == 0:
                    first_line += 1
                    ID, name, score1, score2, score3 = line.split(',')
                    
                else:
                    first_line += 1
                    line = line.strip()
                    ID, name, score1, score2, score3 = line.split(',')
                    name = name.strip()
                    score1 = score1.strip()
                    score2 = score2.strip()
                    score3 = score3.strip()
                    if int(score2) < 0:
                        with open('student.txt', 'r') as file :
                            filedata = file.read()
                            
                        # Replace 
                        filedata = filedata.replace(score2, '0')
                        
                        # New Write
                        with open('student.txt', 'w') as file:
                            file.write(filedata)
                            
                    ID_list.append(ID)
                    name_list.append(name)
                    dict_score[ID] = list(map(str,(score1,score2,score3)))
                    assert int(score1) >= 0 ,'Check data at line {}[{}]'.format(first_line,line)
                    assert int(score2) >= 0 ,'Check data at line {}[{}]'.format(first_line,line)
                    assert int(score3) >= 0 ,'Check data at line {}[{}]'.format(first_line,line)
                    
                        
                    
            except ValueError:
                line = line.strip()
                print('At line {}, an invalid data is found, and it was skipped. [{}]'.format(first_line,line))
                

except IOError:
    print('Cannot open "{}"'.format(file))

else:
    print('The data in file contains {} records.'.format(len(ID_list)))
    for i in range(0,len(ID_list)):
        print('========== {} =========='.format(i+1))
        print('ID: {}'.format(ID_list[i]))
        print('Name: {}'.format(name_list[i]))
        dict_score[ID_list[i]] = ', '.join(dict_score[ID_list[i]])
        print('Score:',dict_score[ID_list[i]])
