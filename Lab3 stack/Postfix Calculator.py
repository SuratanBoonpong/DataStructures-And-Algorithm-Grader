'''จงเขียนโปรแกรมโดยใช้ Stack เพื่อคำนวณหา ค่าของนิพจน์แบบ postfix 

โดยให้แสดงผลลัพธ์ตามตัวอย่าง



class Stack():

    def __init__(self, ls = None):

    def push(self,i):

    def pop(self):

    def isEmpty(self):

    def size(self):

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())



print("Answer : ",'{:.2f}'.format(postFixeval(token)))'''

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

    #def returnStack(self):  
        #return self.items

def postFixeval(st):

    s = Stack()
    for i in st:
        if i == '+':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) + float(obj1)
            s.push(obj)
        elif i == '-':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) - float(obj1)
            s.push(obj)
        elif i == '*':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) * float(obj1)
            s.push(obj)
        elif i == '/':
            obj1 = s.pop()
            obj2 = s.pop()
            obj = float(obj2) / float(obj1)
            s.push(obj)
        else:
            s.push(i)
        #print(s.returnStack())
    return s.pop()

            
print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))