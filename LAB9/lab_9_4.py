inp = "Structured Programming for Information Technology"
inp = inp.lower()
inp = inp.replace(" ","")
output={}
for i in inp:
    count=inp.count(i)
    output[i]=count
output=sorted(output.items())
output=dict(output)
for key,value in output.items():
    print(key+':'+str(value))
