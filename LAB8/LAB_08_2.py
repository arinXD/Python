list_subject=[]
list_score=[]
for i in range(0,5):
    subject=input('Subject: ')
    list_subject.append(subject)
    score=input('Score: ')
    list_score.append(score)
max_subject=list_subject[list_score.index(max(list_score))]
min_subject=list_subject[list_score.index(min(list_score))]
print('Max subject:',max_subject,'score',max(list_score),'\n'+'Min subject:',min_subject,'score',min(list_score))
