a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
s = (a+b+c)/2
s1 = s-a
s2 = s-b
s3 = s-c
triangle_are = (s*s1*s2*s3)**0.5
print('%.2f'%triangle_are)


