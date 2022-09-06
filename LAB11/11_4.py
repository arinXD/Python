def sum(num):
    if num == []:
        return 0
    else:
        return num[0]+sum(num[1:])
            

num_list = [2, 3, 4, 5, 6]
print("Summation:", sum(num_list))
