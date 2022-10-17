number = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
result = [str(i) for i in number if i%2==0 and i>10]
print("RESULT:",", ".join(result))

std = {
    "00":10,
    "01":20,
    "02":50,
    "03":100,
    "04":80,
    "05":90,
    "06":65,
    }
result={k:v for k,v in std.items() if int(k)%2==0}
print("Total: {}\nItem: {}\nAverage: {}".format(len(result),", ".join(result.keys()),sum(result.values())/len(result))
)

"""text = sorted("Structured Programming for Information Technology".lower().replace(" ",""))
result = dict()
for char in text:
    result.setdefault(char,0)
    result[char] += 1
for item in sorted(result.items(),reverse=False,key=lambda item:item[0]):
    print("{} : {}".format(item[0],item[1]))"""

text = sorted("Structured Programming for Information Technology".lower().replace(" ",""))
reverse = dict()
for i in text:
    reverse.setdefault(i,0)
    reverse[i]+=1
for key,val in sorted(reverse.items(),reverse=True,key=lambda item:item[1]):
    print(key,":",val)
