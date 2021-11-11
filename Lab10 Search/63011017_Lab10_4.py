import math

class hash:

    def __init__(self,tableSize,maxCol,threshold):
        self.items = [None]*tableSize
        self.oldInput = []
        self.tableSize = tableSize
        self.maxCol = maxCol
        self.threshold = threshold

    def isFull(self):
        for i in self.items:
            if i == None:
                return False
        return True

    def findQuadraticProbingIndex(self,number):
        qpn = number%self.tableSize
        numCol = 0
        while self.items[qpn] != None:
            numCol += 1
            print("collision number "+str(numCol)+" at "+str(qpn))
            if numCol >= self.maxCol:
                print("****** Max collision - Rehash !!! ******")
                self.Rehash()
                self.insert(number)
                return None
            qpn = (number+pow(numCol,2))%self.tableSize
        return qpn

    def isPrime(self,num):
        for i in range(2,int(math.sqrt(num))+1):
            if num%i == 0:
                return False
        return True

    def leastPrimeNumberMoreThanTwoTimesInputNumber(self,num):
        i = num*2 + 1
        while self.isPrime(i) == False:
            i += 1
        return i

    def insert(self,num):
        index = self.findQuadraticProbingIndex(num)
        if self.isOverThresholdIfAdd():
            print("****** Data over threshold - Rehash !!! ******")
            self.Rehash()
            self.insert(num)
        elif index != None:
            self.items[index] = num
            self.oldInput.append(num)

    def Rehash(self):
        oldList = self.oldInput
        oldSize = len(self.items)
        self.items = [None] * self.leastPrimeNumberMoreThanTwoTimesInputNumber(oldSize)
        self.tableSize = len(self.items)
        self.oldInput = []
        for i in oldList:
            if i != None:
                self.insert(i)
        
    def sizeOfHash(self):
        count = 0
        for i in self.items:
            if i != None:
                count += 1
        return count
    
    def isOverThresholdIfAdd(self):
        if ((self.sizeOfHash()+1)*100)/self.tableSize > self.threshold:
            return True
        else:
            return False

    def printTable(self):
        for i in range(len(self.items)):
            print('#'+str(i+1)+"	"+str(self.items[i]))
        print("----------------------------------------")

print(" ***** Rehashing *****")
condition,data = input("Enter Input : ").split("/")
sizeOfTable,maxCollision,threshold = map(int,condition.split())
h = hash(sizeOfTable,maxCollision,threshold)
print("Initial Table :")
h.printTable()
for i in data.split():
    print("Add : "+str(i))
    h.insert(int(i))
    h.printTable()