grade = float(input("Please enter your grade : " ))

if grade>4.00:
    print("ยินดีด้วยคุณเก่งเที่ยบเท่ามนุษย์ต่างดาว")
elif grade>=3.75:
    no_d = str(input("เคยได้ D ไหม (Y/N) : "))
    if no_d=="n" or no_d=="N":
        print("ยินดีด้วยคุณได้เกียรตินิยมอันดับ 1")
    elif no_d=="y" or no_d=="Y":
        print("เสียใจด้วยคุณไม่ได้เกียรตินิยม")
    else:
        print("***กรุณาพิมพ์(Y/N)***")
elif grade>=3.50:
    no_d = str(input("เคยได้ D ไหม (Y/N) : "))
    if no_d=="n" or no_d=="N":
        print("ยินดีด้วยคุณได้เกียรตินิยมอันดับ 2")
    elif no_d=="y" or no_d=="Y":
        print("เสียใจด้วยคุณไม่ได้เกียรตินิยม")
    else:
        print("***กรุณาพิมพ์(Y/N)***")
else :
    print("เสียใจด้วยคุณไม่ได้เกียรตินิยม")
