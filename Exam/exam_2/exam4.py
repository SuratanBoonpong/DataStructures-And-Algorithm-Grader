class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = ''
        p = self.head
        while p.next != None :
            s += str(p.data)+' <- '
            p = p.next
        return s + str(p.data)

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def reOrder(self,i):
        if i == 0:
            return 
        newHead = self.nodeAt(i)
        temp = self.head
        newTail = self.nodeAt(i-1)
        newTail.next = None
        self.tail.next = temp
        self.head = newHead
        self.tail = newTail
    
print(" *** Re order ***")
l = input('Enter Input : ').split(" ")
ll = LinkedList()
index = 0
for i in l:
    ll.append(i)
print('Before : '+str(ll))
for i in range(ll.size):
    if int(ll.nodeAt(i).data) == 0:
        index = i
        break
ll.reOrder(i)
print('After : '+str(ll))