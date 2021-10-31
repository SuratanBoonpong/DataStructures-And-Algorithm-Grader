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
            self.loop = False
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
    def setNext(self,i,j):
        if int(i) > len(self)-1:
            if len(self) == 0:
                print("Error! {list is empty}")
            else:
                print("Error! {index not in length}: "+str(i))
        elif int(j) > len(self)-1:
            self.append(int(j))
            print("index not in length, append : "+str(j))
        else:
            p = self.nodeAt(int(i))
            n = self.nodeAt(int(j))
            p.next = n
            n.prev = p
            if i < j:
                self.size -= int(j)-int(i)-1
            else:
                self.loop = True
            print("Set node.next complete!, index:value = {0}:{1} -> {2}:{3}".format(str(i),str(p.data),str(j),str(n.data)))

    def delete(self,i) :
        self.remove(self.nodeAt(i))
ans = DoublyLinkedList()
l = input("Enter input : ").split(",")
for i in l:
    command,num = i.split()
    if command == 'A':
        ans.append(num)
        print(ans)
    elif command == 'S':
        fst,snd = num.split(":")
        ans.setNext(fst,snd)
if ans.loop == False:
    print("No Loop")
    if len(ans) != 0:
        print(ans)
    else:
        print("Empty")
else:
    print("Found Loop")
