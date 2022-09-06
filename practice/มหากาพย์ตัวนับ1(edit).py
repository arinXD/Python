name = input('กรอกชื่อ: ')
name = name.lower()
output = {}
show = []
name = name.replace(' ','') #delete white space
output.setdefault('a',0)
output.setdefault('b',0)
for charactor in name:
    
    if charactor not in output:
        pack = {charactor : 1}
        output.update(pack)
    else:
        output[charactor] += 1

for key,value in output.items():
    member = key+' = '+str(value)
    member = member.upper()
    show.append(member)

show = sorted(show)
for i in show:
    print(i)
