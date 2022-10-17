def checked_mirror(items):
    result = [i for i in items if i[::-1].casefold()==i.lower()]
    print("Mirror words: {}".format(", ".join(result)))
    
#problem1
list_input = ["aloha", "wow", "Level", "step on no pets"]
result = [i for i in list_input if i==i[::-1]]
checked_mirror(list_input)
list_input = ["mom", "cat", "suMmer", "Civic"]
result = [i for i in list_input if i.lower()==i[::-1].lower()]
print(result)

#problem 2
num1 = [10, 11, 15, 12, 9, 14, 7]
result = [str(i) for i in range(min(num1)+1,max(num1)) if i not in num1]
print(", ".join(result))
num2 = [12, 5, 9, -3]
result = [str(item) for item in range(min(num2),max(num2)) if not item in num2]
print(", ".join(result))
