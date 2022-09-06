wide = int(input("ความกว้าง(เมตร) : "))
long = int(input("ความยาว(เมตร) : "))
area = wide*long
plot = area/1600
price = plot*1000

import math

print("พื้นทีไร่ :",math.ceil(plot))

if price<=10000:
    print("ยอดเงินช่วยเหลือ :",price)
else:
    print("ยอดเงินช่วยเหลือ : 10000")
