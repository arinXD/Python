data=[]
while True:
    input_letter = input('INPUT: ')
    input_letter = input_letter.lower()
    if input_letter=='00' or input_letter=='0':
        print('a',str(a)+'\n'+'b',str(b))
        break
    data.append(input_letter)
    a=data.count('a')
    b=data.count('b')
    c=data.count('c')
    d=data.count('d')
    e=data.count('e')
    f=data.count('f')
    g=data.count('g')
    h=data.count('h')
    i=data.count('i')
    j=data.count('j')
    k=data.count('k')
    l=data.count('l')
    m=data.count('m')
    n=data.count('n')
    o=data.count('o')
    p=data.count('p')
    q=data.count('q')
    r=data.count('r')
    s=data.count('s')
    t=data.count('t')
    u=data.count('u')
    v=data.count('v')
    w=data.count('w')
    x=data.count('x')
    y=data.count('y')
    z=data.count('z')
    fake=0
while 'a' in data:
    if a>=1 :
        data.remove('a')
while 'b' in data:
    if b>=1:
        data.remove('b')
        
for i in range(1):
    if c>=1:
        print('c ',c)
    elif fake==0:
        fake=0
    if d>=1:
        print('d',d)
    if e>=1:
        print('e',e)
    if f>=1:
        print('f',f)
    if g>=1:
        print('g',g)
    if h>=1:
        print('h',h)
    if i>=1:
        print('i',i)
    if j>=1:
        print('j',j)
    if k>=1:
        print('k',k)
    if l>=1:
        print('l',l)
    if m>=1:
        print('m',m)
    if n>=1:
        print('n',n)
    if o>=1:
        print('o',o)
    if p>=1:
        print('p',p)
    if q>=1:
        print('q',q)
    if r>=1:
        print('r',r)
    if s>=1:
        print('s',s)
    if t>=1:
        print('t',t)
    if u>=1:
        print('u',u)
    if v>=1:
        print('v',v)
    if w>=1:
        print('w',w)
    if x>=1:
        print('x',x)
    if y>=1:
        print('y',y)
    if z>=1:
        print('z',z)


