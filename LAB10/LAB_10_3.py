def color_manage(tence):
    output={}
    new_tence=''
    tence=tence.split('-')
    tence=(sorted(tence,reverse=True))
    for key in tence:
        count=tence.count(key)
        output[key]=count
    n_tence=len(tence)
    for i in range(0,n_tence):
        if i!=n_tence-1:
            new_tence+=tence[i]+'-'
        else:
            new_tence+=tence[i]
 
    return 'New sentence = '+str(new_tence)+'\n'+'Counting color = '+str(output)

sentence01 = "blue-green-red-red-blue-yellow-black-white-blue-red-green-black-black-blue"
sentence02 = "blue-blue-blue-blue-red-red-green-green-white-white"
#print(color_manage(sentence01))
print(color_manage(sentence02))

