list1 = [1, 2, 3, 4, 5, 6]
list2 = [0, 2, 4, 7, 8,]

new = list(filter(lambda a: a in list2 , list1))
if new==[]:
    print('Intersection of the lists: None')
else:
    #new = [2,4] สมาชิกเป็น int
 
    new = ', '.join(map(str,new)) #ก่อน map new = [2,4] เป็น int
                                  #หลัง map new = [ '2' , '4' ] เป็น str
    
    #       'ตัวอักษร'.join() คือการนำสมาชิกในลิสต์ (new) มาต่อกันให้เป็น สตริงสายเดียว
    
    #       เช่น new = ['2','4']
    
    #               ใช้ ''.join()
    
    #           new = '24'
    
    # สมาชิกมันติดกัน ดูไม่รู้เรื่องเลยใส่ , เข้าไปหน้า join
    
    #               ','.join()
    
    #       จะได้ new = '2,4'
    
    print('Intersection of the lists:',new)
    # Intersection of the lists: 2,4
