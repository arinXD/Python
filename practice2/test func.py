v_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4]

for i in v_list:
    print("In loop:", i(3))

print(v_list[0](11))
