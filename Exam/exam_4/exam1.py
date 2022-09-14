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

count = 0
def sumPath(root,value):
    global count
    if root is None:
        return
    value = value + root.data
    if int(value) == int(ans):
            count += 1
    if root.left is None and root.right is None:
        return         

    sumPath(root.left,value)
    sumPath(root.right,value)

T = BST()
lists,ans = input("Enter number / sum : ").split("/")
bstlists = lists.split()
for i in bstlists:
    root = T.insert(int(i))
sumPath(root,0)
if count == 0:
    print("ANS: NO PATH")
else:
    print("ANS:",count)
