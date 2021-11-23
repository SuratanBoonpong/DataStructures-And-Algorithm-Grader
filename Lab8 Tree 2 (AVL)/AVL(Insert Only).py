'''ให้น้องๆสร้าง AVL Tree ด้วย Class โดยผลลัพธ์ให้แสดงเป็น Tree ในแต่ละรอบหลังจาก Insert และปรับ Balance เรียบร้อยแล้ว



** ถ้าสงสัยสามารถดู visualization ของ AVL ได้ที่ website นี้ : https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:

    def __init__(self):
        self.root = None

    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)
        balance = self.height(node.left) - self.height(node.right)
        if balance > 1 and data < node.left.data: #left left
            return self.rightRotate(node)
        if balance < -1 and data >= node.right.data: #right right
            return self.leftRotate(node)
        if balance > 1 and data >= node.left.data: #left right
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)
        if balance < -1 and data < node.right.data: #right left
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        return node

    def height(self,node):
        if node == None:
            return 0
        height_left = self.height(node.left)
        height_right = self.height(node.right)
        if height_left > height_right:
            return height_left + 1
        else:
            return height_right + 1

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

avl = AVL()
lists = list(map(int,input("Enter Input : ").split(" ")))
for i in lists:
    print("Insert : "+"( "+str(i)+" )")
    avl.root = avl.insert(avl.root,i)
    avl.printTree(avl.root)
    print("--------------------------------------------------")
    