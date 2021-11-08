
class Node:

    def __init__(self, data,freq): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None
        self.freq = freq

    def __str__(self):
        return str(self.data) 

class Tree:
    def __init__(self):
        self.root = None
        self.num = 0

    def insert(self, val,freq):  
        if self.root == None:
            self.root = Node(val,freq)
            self.num += 1
        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val,freq)
                self.num+=1
            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val,freq)
                self.num+=1
            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val,freq)
                else:
                    insert_subtree(current.right,self.num - pow(2,h),val,freq)
                self.num+=1

def insert_subtree(r,num,val,freq):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r
        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val,freq)
            return
        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val,freq)
            return
        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val,freq)
        else:
            insert_subtree(current.right,num - pow(2,h),val,freq)
    else:
        return

def height(root):
    if root == None:
        return -1
    else:
        left = height(root.left)
        right = height(root.right)
        if left>right:
            return left + 1
        else:
            return right + 1

def search(node,freq):
    if node == None:
        return []
    s = search(node.left,freq)
    if node.freq == freq:
        s += [node]
    s += search(node.right,freq)
    return s

def sum(node):
    if node == None:
        return 0
    s = sum(node.left) + int(node.data) + sum(node.right)
    return s

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

mondstadt = Tree()
lists,leader = input("Enter Input : ").split("/")
member = lists.split()
for i in range(len(member)):
    mondstadt.insert(member[i],i)
print(sum(mondstadt.root))
for i in leader.split(','):
    left,right = i.split()
    sumLeft = sum(search(mondstadt.root,int(left))[0])
    sumRight = sum(search(mondstadt.root,int(right))[0])
    if sumLeft < sumRight:
        print(left+"<"+right)
    elif sumLeft == sumRight:
        print(left+"="+right)
    elif sumLeft > sumRight:
        print(left+">"+right)