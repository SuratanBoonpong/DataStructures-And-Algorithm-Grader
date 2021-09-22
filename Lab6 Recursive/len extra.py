'''ให้นักศึกษาเขียนฟังก์ชันที่ทำงานเหมือนกับฟังก์ชัน len() เพื่อหาความยาวของ string และแสดงผลดังตัวอย่าง(print ตัวอักษรตามด้วยเครื่องหมายพิเศษสลับกันคู่คี่)

****ห้ามใช้คำสั่ง len, for, while, do while, split*****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 1 ตัว'''
def length(txt):
    if txt == '':
        print("")
        return 0
    elif txt[1::] == '':
        print(txt[0]+"*")
        return 1
    print(txt[0]+"*"+txt[1]+"~",end="")
    return 2+length(txt[2::])

string = input("Enter Input : ")
print(str(length(string)))