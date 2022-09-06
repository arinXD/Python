label = input('Enter: ')
a,A = label.count('a'),label.count('A')
b,B = label.count('b'),label.count('B')
TA,TB = a+A,b+B
allch = len(label)
output = (allch-TA)-TB
print(
    'A = '+(str(TA))+'\n'+
      'B = '+(str(TB))+'\n'+
      'other character = '+str(output)
      )
