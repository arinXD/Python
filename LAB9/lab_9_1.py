var01 = [1, 3, 5, 7, 9]
var02 = [2, 4, 6, 8, 10]
result = {}
for i in range(3,25,3):
    if i%2==0:
        result[i] = list(var01)
    else:
        result[i] = list(var02)
var01[1] = -1
print(result)
