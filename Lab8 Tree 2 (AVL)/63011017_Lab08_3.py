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

    def Rank(self,node,data):
        if node == None:
            return 0
        rank = 0
        rank += self.Rank(node.left,data)
        if node.data <= data:
            rank += 1
        rank += self.Rank(node.right,data)
        return rank

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

bst = BST()
lists,k = input("Enter Input : ").split("/")
for i in lists.split():
    root = bst.insert(int(i))
bst.printTree(root)
print("--------------------------------------------------")
print("Rank of "+k+" : "+str(bst.Rank(root,int(k))))