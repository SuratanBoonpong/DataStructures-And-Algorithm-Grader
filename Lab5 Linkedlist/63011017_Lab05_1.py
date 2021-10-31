

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.siz = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            self.head = self.Node(item)
            self.siz += 1
        else:
            p = self.head
            for i in range(0,self.siz-1):
                p = p.next
            q = self.Node(item)
            p.next = q
            self.siz += 1

    def addHead(self, item):
        if self.isEmpty():
            p = self.Node(item)
            self.head = p
            self.siz += 1
        else:
            p = self.Node(item)
            p.next = self.head
            self.head = p
            self.siz += 1

    def search(self, item):
        if self.index(item)>=0:
            return "Found"
        else:
            return "Not Found"

    def index(self, item):
        p=self.head
        for i in range(self.size()):
            if p.value == item:
                return i
            p = p.next
        return -1

    def size(self):
        return self.siz

    def pop(self, pos):
        if pos < 0 or pos >= self.siz:
            return "Out of Range"
        if pos == 0 and self.siz > 0:
            self.head = self.head.next
            self.siz -= 1
            return "Success"
        else:
            p = self.head
            for i in range(0,pos-1):
                p = p.next 
            p.next =p.next.next
            self.siz -= 1
            return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)