while True:
    try:
        number = int(input('Enter number: '))

    except ValueError:
        print('\n'+'*** Enter number. ***'+'\n')

    else:
        if number == 0:
            break
        else:
            count = 1
            result = 0
            while count != (number+1) :
                if number % count == 0:
                    result += 1
                    count += 1
                else:
                    count += 1
            if result == 1:
                print('\n'+'\t'+'1 is not prime number.'+'\n')

            elif result == 2:
                print('\n'+'\t'+'{} is primt number.'.format(number)+'\n')

            else:
                print('\n'+'\t'+'{} is composit number.'.format(number)+'\n')
