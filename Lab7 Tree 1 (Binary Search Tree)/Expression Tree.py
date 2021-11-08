'''ให้น้องๆรับ input เป็น postfix จากนั้นให้แปลงเป็น Expression Tree , Infix และ Prefix  โดย Operator จะมีแค่ + - * /'''
class Node:
    def __init__(self, data,left=None,right=None): 
        self.data = data  
        self.left = left  
        self.right = right  

    def __str__(self):
        return str(self.data) 

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

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)
s = Stack()

def infix(node):
        if node == None:
            return ''
        s = '' 
        if node.left is not None or node.right is not None:
            s+='('
        s+=infix(node.left)+str(node.data)+infix(node.right)
        if node.left is not None or node.right is not None:
            s+=')'
        return s

def prefix(node):
    if node == None:
        return ''
    s = ''
    s += str(node.data)
    s += prefix(node.left)
    s += prefix(node.right)
    return s

postfix = input("Enter Postfix : ")
for i in range(len(postfix)):
    if postfix[i] in '+-*/':
        node1 = s.pop()
        node2 = s.pop()
        s.push(Node(postfix[i],node2,node1))
    else:
        s.push(Node(postfix[i]))
root = s.pop()
print("Tree :")
printTree(root)
print("--------------------------------------------------")
print("Infix : "+infix(root))
print("Prefix : "+prefix(root))
