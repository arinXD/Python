tell = "089-843-4477"
x1=tell[0:3]
x2=tell[4:7]
x3=tell[8:12]

tell = tell.split('-')
new = ''
for i in tell:
    new += i
    
print(new)
print(x1+x2+x3)
