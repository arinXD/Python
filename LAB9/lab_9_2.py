var01 = {-100:"Alpha", 1:"Brovo", -5:"Charlie"}
var02 = {1.25:"Delta", -2.1:"Echo", 9:"Foxtrot"}
var03={}
#var01.update(var02)
for key,value in var01.items():
    var03[key]=value
for key,value in var02.items():
    var03[key]=value
var03=sorted(var03.items(),reverse=True)
print(dict(var03))

