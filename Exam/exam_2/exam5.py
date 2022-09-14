class Queue:
    def __init__(self,List = None):
        if List == None:
            self.items = []
        else :
            self.items = List

    def __str__(self):
        if len(self) == 0:
            return 'Empty Queue'
        s = 'Queue data : '
        for i in self.items:
            s += str(i) + ' '
        return s

    def __len__(self):
        return len(self.items)

    def enQueue(self,data):
        self.items.append(data)

    def deQueue(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []

    def checkDuplicate(self):
        copy = self.items
        copy.sort()
        for i in range(1,len(copy)):
            if copy[i] == copy[i-1]:
                return 'Duplicate'
        return 'NO Duplicate'

book,DandE = input('Enter Input : ').split("/")
List = book.split(" ")
q = Queue(List)
command = DandE.split(",")
for i in command:
    temp = i.split(" ")
    if temp[0] == 'E':
        q.enQueue(temp[1])
    elif temp[0] == 'D':
        q.deQueue()
print(q.checkDuplicate())