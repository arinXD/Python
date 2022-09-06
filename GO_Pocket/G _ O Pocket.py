def login():
    ######################### check login #####################
    ### main data ###
    global u
    global p
    global t
    global a
    global e
    u = [] 
    p = [] 
    t = [] 
    a = [] 
    e = []
    with open('data.txt', 'r') as db:
        for i in db:
            user, pas, id_user, amount,enter = i.split(',')
            u.append(user)
            p.append(pas)
            t.append(id_user)
            a.append(amount)
            e.append(enter)      
    data_password = dict(zip(u, p)) #passwords 
    data_id = dict(zip(u, t))       #id
    data_amount = dict(zip(u, a))   #money
    ############################################################
    print('\n')
    print("="*75)
    print(' ' * 33 + 'Login!!')
    print('=' *75)
    Username = input('Account name : ')
    Password = input('Password     : ')
    
    if Username in u:
        index = u.index(Username)
    
    if Username == 'Admin' and (Password == '136635' or Password == '4206'):
        def menu_admin():
            print('Account & ID  : a')
            print('Average money : b')
            print('Exit : exit\n')
            menu = input('menu: ')
            
            if menu == 'a' or menu == 'A':
                print('\n'+'='*50)
                print('\n'+' '*18+'Account'+' & '+'ID\n')
                for i in range(0,len(u)):
                    print(str(i+1)+') '+u[i]+' : '+t[i])
                print('-'*50)
                menu_admin()
                
            elif menu == 'b' or menu == 'B':
                total=0
                print('\n'+'='*50)
                for i in a:
                    total += int(i)
                int_money = list(map(int,a))
                print('Average money:','%.2f'%(total/len(a)))
                print('Min:','%.2f'%min(int_money))
                print('Max:','%.2f'%max(int_money))
                print('-'*50)
                menu_admin()
                
            elif menu == 'exit' :
                return True
            else:
                menu_admin()
                
        print('\n'*2+'=' * 50 + '\n')
        print(' ' * 18 + 'G & O POCKET\n')
        print(' ' * 19 +'Management')
        print('-' * 50)
        menu_admin()
        
    def menu_login():
        print('\nCheck amount: 1      Change password : change')
        print('Deposit     : 2      Logout : logout')
        print('Withdrawn   : 3')
        print('Transfer    : 4')
        print('Transaction : 5\n')

        menu = input('Menu: ')
        menu = menu.lower()
        
        #### check amount ####
        if menu == '1' :
            print("")
            print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
            print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
            print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
            print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
            print("-"*75)
            print('Name : ' + Username)
            print('ID     : ' + data_id[Username])
            print('Amount :', data_amount[Username],'THB.')
            print('-'*75)
            menu_login()
        ######################################################
                    
        #### Deposit ####
        elif menu == '2':
            print("")
            print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
            print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
            print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
            print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
            print("-"*75)
            print('Name : ' + Username)
            print('ID     : ' + data_id[Username])
            print('Amount :', data_amount[Username],'THB.')
            print('-'*75)

            deposited = input('Cash : ')
            password_deposit = input('Password : ')

            if deposited.isnumeric()==False:
                print('\n### Please enter integer. ###')
                menu_login()

            elif int(deposited) == 0 :
                print('\n### Do not enter 0. ###')
                menu_login()
                
            #deposited succeed
            elif data_password[Username] == password_deposit:

                a[index] = int(deposited) + int(a[index])
                a[index] = str(a[index])
                
                data_amount[Username] = int(a[index])
                
                print('-' * 50)
                print(' ' * 19 + 'Success!\n')
                print('Cash :',deposited,'THB.')
                print('\nYour balance :' , data_amount[Username],'THB.')
                print('-' * 50)

                
                now = str(datetime.now())
                now = now[:16]
                with open('date.txt','a') as date:
                    date.write(now+','+Username+','+'Deposit   : '+deposited+'\n')
                    
                menu_login()
                
            else:
                print('\n### Incorrect password. ###')
                menu_login()
        #############################################################################

        #### Withdrawn ####
        elif menu == '3':
            print("")
            print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
            print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
            print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
            print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
            print("-"*75)
            print('Name : ' + Username)
            print('ID     : ' + data_id[Username])
            print('Amount :', data_amount[Username],'THB.')
            print('-'*75)

            withdrawn = input('Cash : ')
            password_withdrawn = input('Password : ')
                
            if withdrawn.isnumeric()==False:
                print('\n### Please enter integer. ###')
                menu_login()
                    
            elif int(data_amount[Username]) - int(withdrawn) < 0:
                print('\n### Insufficient funds. ###')
                menu_login()

            elif int(withdrawn) == 0:
                print('\n### Do not enter 0. ###')
                menu_login()
                
            #withdraw succeed        
            elif data_password[Username] == password_withdrawn :

                a[index] = int(a[index]) - int(withdrawn)
                a[index] = str(a[index])
                
                data_amount[Username] = int(a[index])
                
                print('-' * 50)
                print(' ' * 19 + 'Success!\n')
                print('Cash :',withdrawn,'THB.')
                print('\nYour balance :' , data_amount[Username],'THB.')
                print('-' * 50)

                
                now = str(datetime.now())
                now = now[:16] 
                with open('date.txt','a') as date:
                    date.write(now+','+Username+','+'Withdrawn : '+withdrawn+'\n')
                menu_login()
                    
            else:
                print('\n### Incorrect password. ###')
                menu_login()
        ###########################################################################

        #### Tranfer ####
        elif menu == '4':
            print("")
            print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
            print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
            print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
            print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
            print("-"*75)
            print('Name : ' + Username)
            print('ID     : ' + data_id[Username])
            print('Amount :', data_amount[Username],'THB.')
            print('-'*75)
                
            tranfer_id = input('ID (คนรับ): ')
            tranfer_input = input('Cash: ')
            password_tranfer = input('Password: ')

            if tranfer_id not in t:
                print('\n### This ID was not found. ###')
                menu_login()
            else:
                index_tranfer = t.index(tranfer_id)

            if tranfer_input.isnumeric()==False:
                print('\n### Please enter positive integer. ###')
                menu_login()

            elif int(tranfer_input) == 0:
                print('\n### Do not enter 0. ###')
                menu_login()

            elif tranfer_id == data_id[Username]:
                print('\n### Please enter other ID. ###')
                menu_login()

            elif int(data_amount[Username])-int(tranfer_input)<0:
                print('\n### Insufficient funds. ###')
                menu_login()
                             
            elif data_password[Username] == password_tranfer: 
                #เงินเขา
                a[index_tranfer] = int(tranfer_input) + int(a[index_tranfer])
                a[index_tranfer] = str(a[index_tranfer])
                #เงินเรา
                a[index] = int(a[index]) - int(tranfer_input)
                a[index] = str(a[index])
                
                data_amount[Username] = a[index]
                
                print('-' * 50)
                print(' ' * 19 + 'Success!\n')
                print('Name: '+Username)
                print('ID: '+data_id[Username])
                print('\n To\n')
                print('Name: '+u[index_tranfer])
                print('ID: '+tranfer_id+'\n')
                print('Cash: ',tranfer_input)
                print('Your balance: ' + data_amount[Username],'THB.')
                print('-' * 50)
                    
                
                now = str(datetime.now())
                now = now[:16] 
                with open('date.txt','a') as date:
                    date.write(now+','+Username+','+'Tranfer(-)'+': '+tranfer_input+'\n')
                    date.write(now+','+(u[index_tranfer])+','+'Tranfer(+)'+': '+tranfer_input+'\n')

                menu_login()
                    
            else:
                print('\n### Incorrect password. ###')
                menu_login()
        ############################################################################################

        #### Transaction ####
        elif menu == '5':
            print("")
            print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
            print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
            print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
            print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
            print("-"*75)
            print('Name : ' + Username)
            print('ID     : ' + data_id[Username])
            print('Amount :', data_amount[Username],'THB.')
            print('-'*75)
            print('   Date        Time     Transaction\n')
            with open('date.txt','r') as date:
                for line in date:
                    Date, name, transaction = line.split(',')
                    transaction = transaction.strip()
                    year, month, date = Date.split('-')
                    day, time = date.split(' ')
                    if name == Username:
                        print(day+'/'+month+'/'+year+'    '+time+'    '+transaction)         
            print('\n'+'-' * 50)
            menu_login()
        ######################################################
                
        #### end ####
        elif menu == 'logout':
            print('')
            new_data = []
            for i in range(0,len(u)):
                #print(u[i],a[i])#test system
                new_data.append(u[i]+','+p[i]+','+t[i]+','+a[i]+','+e[i])

            with open('data.txt','w') as new_db:
                new_db.writelines(new_data)
            return True
        #######################################

        #### change password ####
        elif menu == 'change':
            print('\n'+'=' * 50 + '\n')
            print(' ' * 15 + '"Change password!"\n')
            print('-' * 50)
                
            old_pass = input('Old password : ')
            new_pass = input('New password : ')
            confirm = input('Confirm password : ')

            if old_pass != data_password[Username] :
                print('\n### Incorrect password. ###')
                menu_login()
                    
            elif new_pass != confirm :
                print("\n### Password don't match. ###")
                menu_login()

            elif new_pass == old_pass :
                print('\n### Duplicate passwords. ###')
                menu_login()
                
            #change succeed
            else:                
                p[index] = new_pass
                list_in_change = []
                for i in range(0,len(u)):
                    list_in_change.append(u[i]+','+p[i]+','+t[i]+','+a[i]+','+e[i])

                with open('data.txt','w') as new_pass:
                    new_pass.writelines(list_in_change)
                print('\n*** Success! ***')
                print('*** Please Re-Login ***')
                return True
            
        ##################################################
                
        #Enter other key             
        else:
            print('\n### Please enter menu. ###') 
            menu_login()
            
    #login succes          
    if Username in data_password and data_password[Username] == Password:
        print("")
        print('   ___        ___          ___    ___     ___   _  __  ___   _____ ')
        print('  / __|      / _ \        | _ \  / _ \   / __| | |/ / | __| |_   _|')
        print(" | (_ |  _  | (_) |  _    |  _/ | (_) | | (__  | ' <  | _|    | |  ")
        print("  \___| (_)  \___/  (_)   |_|    \___/   \___| |_|\_\ |___|   |_|")
        print("-"*75)
        print('Name : ' + Username)
        print('-'*75)
        menu_login()
        
    #wrong name,password      
    else:       
        if Username != 'Admin':
            print('\n### Incorrect name or password. ###\n')
        else:
            print() ###end present###

def register():
    ##### check regis #####
    um = [] #user list
    tm = [] #ID list

    with open('data.txt', 'r') as db:
        for i in db:
            user, pas, id_user, amount,enter = i.split(',')
            um.append(user)
            tm.append(id_user)
    #############################
    print("="*75)
    print(' ' * 20 + 'Welcome To Registration!!')
    print('=' *75)
    
    Username = input('Create account name: ')    
    Password = input('Create password: ')
    confirm = input('Confirm password: ')
    id1 = input('Create ID number(6 character): ')

    if Username in um:
        print("\n"+' ' * 20 +" -----------------------------")
        print(' ' * 20      +'| Account name has been taken |')
        print(' ' * 20      +" -----------------------------"+"\n")
        return True
    
    elif Password != confirm:
        print("\n"+' ' * 20 +" ----------------------------")
        print(' ' * 20      +"| The password doesn't match |")
        print(' ' * 20      +" ----------------------------"+"\n")
        return True

    elif id1.isnumeric() == False:
        print("\n"+' ' * 20 +" ---------------------------- ")
        print(' ' * 20      +"|       ID must be number    |")
        print(' ' * 20      +" ---------------------------- "+"\n")
        return True

    elif len(id1) < 6 or len(id1) > 6:
        print("\n"+' ' * 20 +" ---------------------------- ")
        print(' ' * 20      +"|          Incorrect ID      |")
        print(' ' * 20      +" ---------------------------- "+"\n")
        return True
        
    elif id1 in tm:
        print("\n"+' ' * 20 +" ---------------------------- ")
        print(' ' * 20      +"|      ID has been taken     |")
        print(' ' * 20      +" ---------------------------- "+"\n")
        return True
        
    #regis success
    else:
        with open('data.txt', 'a') as dba:
            dba.write(Username+','+Password+','+id1+','+'0'+','+'\n')
        print("\n"+' ' * 20 +" ---------------------------- ")
        print(' ' * 20      +"|     Registration success   |\n")
        print(' ' * 20      +"|Uersername: "+Username+"    |")
        print(' ' * 20      +"|ID: "+id1+"                 |")
        print(' ' * 20      +" ---------------------------- "+"\n")
        return True
    
def menu():
    while True:
        print("="*75)
        print("░██████╗░░░░░█████╗░░░░  ██████╗░░█████╗░░█████╗░██╗░░██╗███████╗████████╗")
        print("██╔════╝░░░░██╔══██╗░░░  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝")
        print("██║░░██╗░░░░██║░░██║░░░  ██████╔╝██║░░██║██║░░╚═╝█████═╝░█████╗░░░░░██║░░░")
        print("██║░░╚██╗░░░██║░░██║░░░  ██╔═══╝░██║░░██║██║░░██╗██╔═██╗░██╔══╝░░░░░██║░░░")
        print("╚██████╔╝██╗╚█████╔╝██╗  ██║░░░░░╚█████╔╝╚█████╔╝██║░╚██╗███████╗░░░██║░░░")
        print("░╚═════╝░╚═╝░╚════╝░╚═╝  ╚═╝░░░░░░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░")
        print("="*75)
        print('Letters')
        print('R: Registration')
        print('L: Login')
        print('E: Exit\n')

        menu = input('Choose letters: ')
        menu = menu.lower()
        
        if menu == 'l':
            login()
            
        elif menu == 'r':
            register()
            
        elif menu == 'e':
            return;
        
        else:
            print('\n### Enter menu. ###\n')
        
#########################################################################################################
###MAIN PROGRAM###
from datetime import datetime
#start
menu()

#end
print('\n' + '-' * 50)
print('   Just wanted to say thank you for your using.\n\tWe’re so lucky to have user like you!')
print('-' * 50)
