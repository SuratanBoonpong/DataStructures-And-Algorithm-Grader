class DoublyLinkedList :
    class Node :
        def __init__(self,data,prev = None,next = None) :
            self.data = data
            if prev is None :
                self.prev = None
            else :
                self.prev = prev
            if next is None :
                self.next = None
            else :
                self.next = next  
    def __init__(self):                
            self.dummy = self.Node(None,None,None)
            self.dummy.next = self.dummy.prev = self.dummy
            self.size = 0       
    def __str__(self):
        s = ''
        p = self.dummy.next
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
            p = p.next
        if str(p.data) != "None":
            s += str(p.data)
        return s
    def str_reverse(self):
        s = ''
        p = self.nodeAt(len(self)-1)
        for i in range(len(self)-1) :
            s += str(p.data) + '->'
            p = p.prev
        if str(p.data) != "None":
            s += str(p.data)
        return s 
    def __len__(self) :
        return self.size     
    def isEmpty(self) :
        return self.size == 0 
    def indexOf(self,data) :
        q = self.dummy.next
        for i in range(len(self)) :
            if q.data == data :
                return i
            q = q.next
        return -1
    def isIn(self,data) :
        return self.indexOf(data) >= 0
    def nodeAt(self,i) :
        p = self.dummy
        for j in range(-1,i) :
            p = p.next
        return p
    def insert(self,q,data) :
        p = q.prev
        x = self.Node(data,p,q)
        p.next = q.prev = x
        self.size += 1  
    def append(self,data) :
        self.insert(self.nodeAt(len(self)),data)
    def remove(self,q) :
        if self.isIn(q):
            q = self.nodeAt(self.indexOf(q))
            p = q.prev
            x = q.next
            p.next = x
            x.prev = p
            self.size -= 1
            return q
        else:
            return -1
    def delete(self,i) :
        self.remove(self.nodeAt(i))
ans = DoublyLinkedList()
l = input("Enter Input : ")
l = l.replace(", ",",")
l = l.split(",")
for i in l:
    number = i.split()
    command = number[0]
    if number[0] == 'A':
        ans.append(number[1])
    elif number[0] =='Ab':
        ans.insert(ans.nodeAt(0),number[1])
    elif number[0] == 'I':
        index,data = number[1].split(":")
        if int(index) < 0 or len(ans) < int(index):
            print("Data cannot be added")
        else:
            ans.insert(ans.nodeAt(int(index)),data)
            print("index = {0} and data = {1}".format(index,data))
    elif number[0] == 'R':
        idx = ans.indexOf(number[1])
        r = ans.remove(number[1])
        if r==-1:
            print("Not Found!")
        else:
            print("removed : {0} from index : {1}".format(str(r.data),str(idx)))
    print("linked list : " + str(ans))
    print("reverse : "+ans.str_reverse())
