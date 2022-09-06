print('Train Station\nStation 1 = 27\nStation 2 = 35\nStation 3 = 42')
station = int(input('Select Station : '))
price = int(input('Price: '))
coin = 0
count10 = 0
count5 = 0
count2 = 0
count1 = 0

if station == 1:
    station = 27
    coin = price-station
    while True:
        if coin>=10:
                coin -= 10
                count10 += 1

        elif coin>=5:
                coin -= 5
                count5 += 1

        elif coin>=2:
                coin -= 2
                count2 += 1

        elif coin>=1:
                coin -= 1
                count1 += 1
        else:
            break    
    print('เหรียญ 10 :',count10,'เหรียญ'+'\n'+'เหรียญ 5 :',count5,'เหรียญ'+'\n'+
          'เหรียญ 2 :',count2,'เหรียญ'+'\n'+'เหรียญ 1 :',count1,'เหรียญ'+'\n'
            )

if station == 2:
    station = 35
    coin = price-station
    while True:
        if coin>=10:
                coin -= 10
                count10 += 1

        elif coin>=5:
                coin -= 5
                count5 += 1

        elif coin>=2:
                coin -= 2
                count2 += 1

        elif coin>=1:
                coin -= 1
                count1 += 1
        else:
            break    
    print('เหรียญ 10 :',count10,'เหรียญ'+'\n'+'เหรียญ 5 :',count5,'เหรียญ'+'\n'+
          'เหรียญ 2 :',count2,'เหรียญ'+'\n'+'เหรียญ 1 :',count1,'เหรียญ'+'\n'
            )

if station == 3:
    station = 42
    coin = price-station
    while True:
        if coin>=10:
                coin -= 10
                count10 += 1

        elif coin>=5:
                coin -= 5
                count5 += 1

        elif coin>=2:
                coin -= 2
                count2 += 1

        elif coin>=1:
                coin -= 1
                count1 += 1
        else:
            break    
    print('เหรียญ 10 :',count10,'เหรียญ'+'\n'+'เหรียญ 5 :',count5,'เหรียญ'+'\n'+
          'เหรียญ 2 :',count2,'เหรียญ'+'\n'+'เหรียญ 1 :',count1,'เหรียญ'+'\n'
            )

