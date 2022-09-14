class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node)
        printTree(node.left, level + 1)

def parents(r,data):
    if int(r.data) == int(data):
        return "none because "+str(data)+" is root!!!"
    cur = r
    while True:    
        if cur.left != None and int(cur.left.data) == int(data):
            return cur.data
        elif cur.right != None and int(cur.right.data) == int(data):
            return cur.data
        elif int(data) < int(cur.data):
            if cur.left == None:
                return 'not found!!!'
            else:
                cur = cur.left
        elif int(data) > int(cur.data):
            if cur.right == None:
                return 'not found!!!'
            else:
                cur = cur.right

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree(tree.root)
print('\nParents of',data[1],'is',parents(tree.root,data[1]))