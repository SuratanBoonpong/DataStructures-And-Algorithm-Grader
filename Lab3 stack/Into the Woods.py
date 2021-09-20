'''กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป

ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

อธิบาย Input :   A  <Heights>  แสดงถึงความสูงของต้นไม้  ,   B  คือการหันหลังกลับมามอง

อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

class Stack:

    ### Enter Your Code Here ###

S = Stack()


inp = input('Enter Input : ').split(',')

### Enter Your Code Here ###'''

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
        
    def returnList(self):
        return self.items

def stackCheck(st):
    S = Stack()
    if len(st)==0:
        return '0'
    else:
        test = int(st[len(st)-1]) 
        S.push(test)
        for i in range(len(st)-2,-1,-1):
            if int(st[i])>test:
                test = int(st[i])
                S.push(test)
        return S.size()
            
S = Stack()
inp = input('Enter Input : ').split(',')
for i in inp:
    l = i.split()
    if l[0]=='A':
        S.push(l[1])
    elif l[0]=='B':
        print(stackCheck(S.returnList()))
