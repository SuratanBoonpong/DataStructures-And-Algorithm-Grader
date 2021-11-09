class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self,items,tableSize,maxCol):
        self.items = items
        self.tableSize = tableSize
        self.maxCol = maxCol

    def isFull(self):
        for i in self.items:
            if i == None:
                return False
        return True

    def findQuadraticProbingIndex(self,number):
        qpn = number%self.tableSize
        numCol = 1
        while self.items[qpn] != None:
            print("collision number "+str(numCol)+" at "+str(qpn))
            if numCol >= self.maxCol:
                print("Max of collisionChain")
                return
            qpn = (number+pow(numCol,2))%self.tableSize
            numCol += 1
        return qpn

    def printTable(self):
        for i in range(len(self.items)):
            print('#'+str(i+1)+"	"+str(self.items[i]))
        print("---------------------------")

def sumOfASCII(string):
    sum = 0
    for char in string:
        sum += ord(char)
    return sum

print(" ***** Fun with hashing *****")
condition,data = input("Enter Input : ").split("/")
sizeOfTable,maxCollision = map(int,condition.split())
Table = [None] * sizeOfTable
h = hash(Table,sizeOfTable,maxCollision)
for i in data.split(","):
    if h.isFull():
        print("This table is full !!!!!!")
        break
    key,value = i.split()
    indexInsert = h.findQuadraticProbingIndex(sumOfASCII(key))
    if indexInsert != None:
        Table[indexInsert] = Data(key,value)
    h.printTable()