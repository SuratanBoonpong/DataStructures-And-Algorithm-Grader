'''ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา

E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

D  ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและ index ของ value นั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

*** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty'''

class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items

q = Queue()
l = input("Enter Input : ").split(',')
for i in l:
    temp = i.split()
    if temp[0]== 'E':
        q.enQueue(temp[1])
        print(str(q.size()))
    elif temp[0]=='D':
        if q.size() == 0:
            print("-1")
        else:
            temp = q.deQueue()
            print(str(temp)+" 0")
if q.size() == 0:
    print("Empty")
else:
    for i in q.returnQueue():
        print(i,end=' ')

