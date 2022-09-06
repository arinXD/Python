A=(100,71,'A')
B=(70,31,'B')
C=(30,0,'C')
score=int(input('SCORE: '))
if A[1] <= score <= A[0]:
    print('Grade:',A[2])
elif B[1] <= score <= B[0]:
    print('Grade:',B[2])
elif C[1] <= score <= C[0]:
    print('Grade:',C[2])
else:
    print('ERROR')
