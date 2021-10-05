'''จงเขียน ฟังก์ชั่นสำหรับการ encode และ decode ของ String ที่รับมาโดยให้ทำเป็นรูปแบบ Queue

รูปแบบการรับ Input โดยจะคั่นแต่ละตำแหน่งด้วย คอมม่า(',') :

    - ตำแหน่งที่หนึ่ง string ไม่จำกัดความยาวโดยที่จะไม่นับช่องว่าง(spacebar)

    - ตำแหน่งที่สอง ชุดตัวเลข(1-9)

โดยที่รูปแบบการ encode คือ การนำ String ที่รับมาเพิ่มค่า ascii เท่ากับค่าของชุดตัวเลขในตำแหน่งแรก หลังจากนั้นให้ dequeue ชุดตัวเลขออกไปไว้ข้างหลังสุด เช่น ตัวอักษรตำแหน่งแรกคือ i และชุดตัวเลขในตำแหน่งแรกคือ 2 ดังนั้นตัวอักษรที่ได้จากการ encode คือ k โดยจะทำการวนชุดตัวเลขไปเรื่อยๆจนกระทั่งทำการ encode ทุกตัวอักษรใน String ครบ ถ้าหากผลลัพธ์จากการเพิ่มหรือลดค่า ascii ไม่ใช่ตัวอักษรให้กลับมาวนในชุดตัวอักษร เช่น อักษร z ทำการ encode ด้วยเลข 2 จะได้ b และหากทำการ decode ตัวอักษร A ด้วย 2 จะได้ Y 

โดยการ decode หลังจาก encode ต้องให้คำตอบที่มีค่าเท่ากับ String เดิมก่อนทำการ encode 

***ให้ใช้วิธี enqueue และ dequeue ในการเลื่อนตำแหน่ง เท่านั้น***

โดยรูปแบบการ run ดังนี้ :

q1 = Queue(string)

q2 = Queue(number)

encodemsg(q1, q2)

decodemsg(q1, q2)'''

class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def copy(self,i):
        self.items = i
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items

def encodemsg(q1, q2):
    enlist = []
    numlist = q2.items.copy()
    for i in range(q1.size()):
        temp = q1.deQueue()
        num = q2.deQueue()
        asci = ord(temp)
        if asci >= 65 and asci <= 90:
            if asci + int(num) > 90:
                asci = 65 + asci + int(num) - 91
                enlist.append(chr(asci))
            else:
                enlist.append(chr(asci + int(num)))
        elif asci >= 97 and asci <= 122:
            if asci + int(num) > 122:
                asci = 97 + asci + int(num) - 123
                enlist.append(chr(asci))
            else:
                enlist.append(chr(asci + int(num)))
        q2.enQueue(num)
    q1.copy(enlist)
    q2.copy(numlist)
    print("Encode message is :  "+str(q1.returnQueue()))

def decodemsg(q1, q2):
    delist = []
    numlist = q2.items.copy()
    for i in range(q1.size()):
        temp = q1.deQueue()
        num = q2.deQueue()
        asci = ord(temp)
        if asci >= 65 and asci <= 90:
            if asci - int(num) < 65:
                asci = 90 - (65 - (asci - int(num))) + 1
                delist.append(chr(asci))
            else:
                delist.append(chr(asci - int(num)))
        elif asci >= 97 and asci <= 122:
            if asci - int(num) < 97:
                asci = 122 - (97 - (asci - int(num))) + 1
                delist.append(chr(asci))
            else:
                delist.append(chr(asci - int(num)))
        q2.enQueue(num)
    q1.copy(delist)
    q2.copy(numlist)
    print("Decode message is :  "+str(q1.returnQueue()))

stri,num = input("Enter String and Code : ").split(',')
stri = stri.replace(" ","")
string = []
number = []
for i in range(len(stri)):
    string.append(stri[i])
for i in range(len(num)):
    number.append(num[i])
q1 = Queue(string)
q2 = Queue(number)
encodemsg(q1, q2)
decodemsg(q1, q2)