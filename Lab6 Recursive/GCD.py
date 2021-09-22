'''เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว

****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****

หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว

บทนิยาม

ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว'''

import math
def gcd(m,n):
    m = abs(m)
    n = abs(n)
    if n==0:
        return m
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
m,n = map(int,input("Enter Input : ").split())
if n<0 and m==0:
    m,n =m,n
elif abs(n)>abs(m):
    m,n = n,m
if m==0 and n==0:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {m} and {n} is : {str(gcd(m,n))}")