class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None

    def __str__(self):
        return str(self.data)

class BST:

    def __init__(self) :
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            cur = self.root
            while True:
                if val < cur.data:
                    if cur.left == None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                elif val > cur.data:
                    if cur.right == None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right
        return self.root

    def Max(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        max = cur.data
        return max

    def Min(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        min = cur.data
        return min
    def printTree(self, node, level = 0):

        if node != None:

            self.printTree(node.right, level + 1)

            print('     ' * level, node)

            self.printTree(node.left, level + 1)



T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:

    root = T.insert(i)

T.printTree(root)

print('-' * 50)
print("Min : "+str(T.Min()))
print("Max : "+str(T.Max()))