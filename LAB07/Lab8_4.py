ID = input('ID: ')
finder = ID.find('-')
before= ID[finder-1]
after= ID[finder+1]
print('ผลลัพธ์:',int(before)+int(after))
