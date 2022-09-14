class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self,node,data):
        if node == None:
            return Node(data)
        if data < node.data:
            node.left = self.insert(node.left,data)
        if data >= node.data:
            node.right = self.insert(node.right,data)
        b = self.height(node.left) - self.height(node.right)
        if b > 1 and data < node.left.data: #left left
            return self.rRotate(node)
        if b < -1 and data >= node.right.data: #right right
            return self.lRotate(node)
        if b > 1 and data >= node.left.data: #left right
            node.left = self.lRotate(node.left)
            return self.rRotate(node)
        if b < -1 and data < node.right.data: #right left
            node.right = self.rightRotate(node.right)
            return self.lRotate(node)
        return node

    def height(self,node):
        if node == None:
            return 0
        hl = self.height(node.left)
        hr = self.height(node.right)
        if hl > hr:
            return hl + 1
        else:
            return hr + 1

    def lRotate(self,z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        return y

    def rRotate(self,z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        return y

    def Inorder(self,node):
        if node == None:
            return ''
        s = ''
        s += self.Inorder(node.left)
        s += str(node.data) + ' '
        s += self.Inorder(node.right)
        return s

    def Preorder(self,node):
        if node == None:
            return ''
        s = ''
        s += str(node.data) + ' '
        s += self.Preorder(node.left)
        s += self.Preorder(node.right)
        return s

    def Postorder(self,node):
        if node == None:
            return ''
        s = ''
        s += self.Postorder(node.left)
        s += self.Postorder(node.right)
        s += str(node.data) + ' '
        return s

    def print_inorder(self):
        print("in_order  --> "+self.Inorder(self.root))

    def print_preorder(self):
        print("preorder  --> "+self.Preorder(self.root))
    
    def print_postorder(self):
        print("postorder --> "+self.Postorder(self.root))

print(" *** AVL Tree ***")    

input_string = input("Enter some numbers : ")

bst = AVLTree()

for n in input_string.split():

	bst.root = bst.insert(bst.root,int(n))

bst.print_inorder()

bst.print_preorder()

bst.print_postorder()