class Queue:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enQueue(self,i):
        self.items.append(i)
    def deQueue(self):
        if len(self.items)>0:
            return self.items.pop(0)
    def copy(self,i):
        self.items = i
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def returnQueue(self):
        return self.items
    def insertQueue(self,data,mark):
        self.temp = []
        for i in range(mark):
            self.temp.append(self.items[i])
        self.temp.append(data)
        for i in range (mark,len(self.items)):
            self.temp.append(self.items[i])
        self.items = self.temp
q = Queue()
order = Queue()
personAndID,command = input("Enter Input : ").split('/')
personAndID = list(personAndID.split(','))
command = list(command.split(','))
for i in command:
    l = i.split()
    if l[0] == 'D':
        if q.size() == 0:
            print("Empty")
        else:
            k = q.deQueue()
            order.deQueue()
            print(k)
    elif l[0] == 'E':
        for j in personAndID:
            t = j.split()
            if t[1]==l[1]:
                mark = q.size()
                for ID in range(order.size()-1,-1,-1):
                    if order.returnQueue()[ID] == t[0]:
                        mark = ID+1
                        break
                if mark == q.size():
                    q.enQueue(t[1])
                    order.enQueue(t[0])
                else:
                    q.insertQueue(t[1],mark)
                    order.insertQueue(t[0],mark)