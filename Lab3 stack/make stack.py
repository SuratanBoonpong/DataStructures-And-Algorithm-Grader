'''ให้นักศึกษา สร้าง class Stack ด้วย list ของ python โดย มี method ดังต่อไปนี้

def __init__()    // ใช้สำหรับสร้าง list ว่าง

def push(i)        // เก็บข้อมูลลง stack

def pop()          // นำข้อมูลออกจาก stack

def isEmpty()   // ตรวจสอบว่า stack ว่างไหม ถ้าว่าง return true ถ้าไม่ว่าง return false

def size()         // ตรวจสอบจำนวนข้อมูลใจ stack



แล้วให้โปรแกรมรับข้อมูล เพื่อเก็บใน stack และให้ทำงานตาม code คำสั่งต่อไปนี้

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)'''

class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)
           
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return str(len(self.items))     

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items)