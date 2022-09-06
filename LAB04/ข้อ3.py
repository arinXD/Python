grade = float(input("Please enter your grade : "))
if grade>4.00 or grade<0:
    print("xxxxxxx")
elif grade>=3.50 and grade<=4.00:
    print("ดีมาก")
elif grade>=2.50 and grade<3.50:
    print("ดี")
elif grade>=1.50 and grade<2.50:
    print("ปานกลาง")
elif grade>=1.00 and grade<1.50:
    print("ปรับปรุง")
else:
    print("ไม่ผ่าน")
