def add_name():
    print('')
    stu_id = input('Enter student id: ')
    stu_name = input('Enter student name: ')
    stu_grade = input('Enter student grade: ')
        
    if stu_id in student_data:
        print('This ID has been taken')
        menu()
    else:
        print('\n*** Success ***')
        with open('students.txt','a') as file:
            file.write(stu_id + ',' + stu_name + ',' + stu_grade + '\n')
            file.close()
            menu()

def show_name():
    print('\nID\tName\tGPA')
    print('='*30)
    total = 0
    with open('students.txt','r') as file:
        for line in file:
            line = line.strip()
            ID, name, gpa = line.split(',')
            print(ID+'\t'+name+'\t'+gpa)
  
    for key,value in student_data.items():
        total += float(value['grade'])
    print('Average of GPA is:','%.2f'%float(total/len(student_data)))
    menu()

def search_id():
    print('')
    UID = []
    Uname = []
    Ugpa = []
    
    search = input('Enter student id: ')
    print('')
    with open('students.txt','r') as file:
        for line in file:
            line = line.strip()
            ID, name, gpa = line.split(',')
            UID.append(ID)
            Uname.append(name)
            Ugpa.append(gpa)
        if search in UID:
            index = UID.index(search)
            print('Student ID:',UID[index])
            print('Student name:',Uname[index])
            print('Student GPA:',Ugpa[index])
            menu()
        else:
            print('This ID was not found.')
            menu()
def menu():
    while True:
        print('')            
        print('='*4+' Select Menu '+'='*4)
        print('1. Add student data')
        print('2. Show student data')
        print('3. Search student data')
        print('4. Exit')
        menu = input('Select menu number [1-4]: ')
        if menu == '1':
            add_name()

        elif menu == '2':
            show_name()
            
        elif menu == '3':
            search_id()
        
        elif menu == '4':
            return True
        else:
            print('Enter 1-4')
############################################################################

student_data = dict()    
with open('students.txt','r') as file:
    for i in file:
        text = i.strip()
        id, name, grade = text.split(',')
        student_data[id] = {'name':name, 'grade':grade}

menu()
exit()
