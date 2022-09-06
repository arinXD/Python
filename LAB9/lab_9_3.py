dict_student = {
 "001":{"sex":"F","GPA":3.50},
 "002":{"sex":"M","GPA":2.67},
 "003":{"sex":"M","GPA":3.28},
 "004":{"sex":"M","GPA":2.75},
 "005":{"sex":"F","GPA":3.21},
 "006":{"sex":"M","GPA":2.62},
 "007":{"sex":"F","GPA":3.00},
 "008":{"sex":"F","GPA":2.30}
 }
GPA=0
F=0
M=0
for value in dict_student.values():
    if value['GPA']<3:
        GPA+=1
        if value['sex']=="F":
            F+=1
        if value['sex']=="M":
            M+=1
print('There are '+str(GPA)+' students who have GPA less than 3.00'+'\n'+
      'Female =',str(F)+'\n'+'Male =',M
      )
