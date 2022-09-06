label = input('Enter: ')
if ' ' in label:
    label = label.split(' ')
    label = label[0]+label[1]
label = label.isalpha()
if label == False:
    print('ผลลัพธ์: มีตัวเลข')
else:
    print('ผลลัพธ์: ไม่มีตัวเลข')
