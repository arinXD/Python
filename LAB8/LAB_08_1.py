list_subject=[]
while True:
    print('----------------\n  MENU\nA : Add sub\nD : Remove\nP : Show subject\nY : End')
    menu=input('----------------\nMenu: ')
    if menu=='a' or menu=='A':
        add_subject=input('----------------\nAdd subject: ')
        if add_subject not in list_subject:
            list_subject.append(add_subject)
        elif add_subject in list_subject:
            print('"already has this subject"')
    elif menu=='d' or menu=='D':
        remove_subject=input('Remove subject: ')
        if remove_subject in list_subject:
            list_subject.remove(remove_subject)
        elif remove_subject not in list_subject:
            print('"This subject was not found"')
    elif menu=='p' or menu=='P':
        len_list=len(list_subject)
        print('----------------\nNO    Subject')
        for i in range(0,len_list+1):
            if i!=len_list:
                print(i+1,'    ',list_subject[i])
    elif menu=='y' or menu=='Y':
        print('END')
        break
    else:
        print('"Error"')
