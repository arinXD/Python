list1 = [1, 2, 3, 4, 5, 6]
list2 = [0, 2, 4, 7, 8,]

new = list(filter(lambda a: a in list2 , list1))
if new==[]:
    print('Intersection of the lists: None')
else:
    new = ', '.join(map(str,new)) 
    print('Intersection of the lists:',new)

