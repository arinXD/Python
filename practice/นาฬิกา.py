time = int(input("Enter Second : "))
minute = time/60
hr = minute/60
day = hr/24
print('"Time"')
print("Second :",time)
print("Minute :",minute)
print("Hour :",'%.2f'%hr)
print("Day :",'%.5f'%day)
