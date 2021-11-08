'''ให้น้องรับ input แล้วนำ input นั้นมาสร้าง Binary Search Tree โดย input ตัวแรกสุดจะเป็น Root เสมอ และหาค่าที่น้อยกว่าค่าที่รับเข้ามาของ Binary Search Tree

***** ห้ามใช้ Built-in Function เช่น min() , max() , sort() , sorted()'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left == None:
                        cur.left = Node(data)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = Node(data)
                        break
                    else:
                        cur = cur.right
        return self.root

    def below(self,node,data): #inorder
        if node == None:
            return ''
        belowlist = ''
        belowlist += self.below(node.left,data)
        if int(node.data) < int(data):
            belowlist += str(node.data) + ' '
        belowlist += self.below(node.right,data)
        return belowlist

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
bst,below = input('Enter Input : ').split("|")
bstlist = [int(i) for i in bst.split(" ")]
for i in bstlist:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
belowlist = T.below(root,below)
if belowlist == '':
    print("Below "+str(below)+" : Not have")
else:
    print("Below "+str(below)+" : "+belowlist)

