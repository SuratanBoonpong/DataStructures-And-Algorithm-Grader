'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้

A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack

P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )

D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  

LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )

การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม

*** Hint ***

ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ'''

def ManageStack(stack):
    result = []
    def A(result,temp):
        result.append(temp)
        print("Add = "+str(temp))
    def P(result):
        if len(result)==0:
            print("-1")
        else:
            temp = result[-1]
            result.pop()
            print("Pop = "+str(temp))
    def D(result,temp):
        num = 0
        if len(result)==0:
            print("-1")
        else:
            for i in result:
                if i == temp:
                    num += 1
            for i in range(num):
                result.remove(temp)
                print("Delete =",str(temp))       
    def LD(result,temp):
        templist = []
        if len(result)==0:
            print("-1")
        else:
            for i in range(len(result)-1,-1,-1):
                if int(result[i])>=int(temp):
                    templist.append(result[i])
                else:
                    print("Delete = "+str(result[i])+" Because "+str(result[i])+" is less than "+str(temp))
        templist.reverse()
        return templist
    def MD(result,temp):
        templist = []
        if len(result)==0:
            print("-1")
        else:
            for i in range(len(result)-1,-1,-1):
                if int(result[i])<=int(temp):
                    templist.append(result[i])
                else:
                    print("Delete = "+str(result[i])+" Because "+str(result[i])+" is more than "+str(temp))
        templist.reverse()
        return templist
    for i in stack:
        L = i.split()
        if L[0]=='A':
            A(result,L[1])
        elif L[0]=='P':
            P(result)
        elif L[0]=='D':
            D(result,L[1])
        elif L[0]=='LD':
            result = LD(result,L[1])
        elif L[0]=='MD':
            result = MD(result,L[1])
    for i in range(0,len(result)):
        result[i] = int(result[i])
    print("Value in Stack = "+str(result))
l = input("Enter Input : ").split(',')
ManageStack(l)