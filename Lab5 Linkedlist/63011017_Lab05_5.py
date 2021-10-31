import math
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = Node(LL[0])
    temp = head
    for i in range(1,len(LL)):
        nxt = Node(LL[i])
        temp.next = nxt
        temp = temp.next
    return head

def printLL(head):
    s = ''
    temp = head
    while temp!=None:
        s += str(temp.value) + ' '
        temp = temp.next
    return s

def SIZE(head):
    temp = head
    size = 0
    while temp!=None:
        temp = temp.next
        size += 1
    return size
    
def scarmble(head, b, r, size):
    indexb = math.floor((size * b) / 100)
    indexr = math.floor((size * r) / 100)
    temp = head
    for i in range(0,indexb-1):
        temp = temp.next
    newHeadBU = temp.next
    findtailBU = newHeadBU
    temp.next = None
    BottomUpHead = newHeadBU
    while (findtailBU.next!=None):
        findtailBU = findtailBU.next
    findtailBU.next = head
    print("BottomUp "+format(b,".3f")+" % : ",end="")
    while (newHeadBU!=None):
        print(newHeadBU,end=" ")
        newHeadBU = newHeadBU.next
    print()

    RiffleHead = BottomUpHead
    if indexr != 1:
        createRf = RiffleHead
        mainRfHead = RiffleHead.next
        temp = BottomUpHead
        for i in range(0,indexr-1):
            temp = temp.next
        newHeadtemp = temp.next
        temp.next = None
        swap = False
        while mainRfHead != None and newHeadtemp != None:
            if mainRfHead != None and newHeadtemp != None:
                if swap == False:
                    createRf.next = newHeadtemp
                    newHeadtemp = newHeadtemp.next
                    createRf = createRf.next
                    swap = True
                elif swap == True:
                    createRf.next = mainRfHead
                    mainRfHead = mainRfHead.next
                    createRf = createRf.next
                    swap = False
        if swap == True:
            createRf.next = mainRfHead
        else:
            createRf.next = newHeadtemp
    print("Riffle "+format(r,".3f")+" % : ",end="")
    print(printLL(RiffleHead))
    DerifHead = RiffleHead
    deRifOdd = RiffleHead
    HeadOdd = RiffleHead
    deRifEven = RiffleHead.next
    HeadEven = RiffleHead.next
    startDerif = RiffleHead.next.next
    minvalue = min(indexr,size-indexr)
    for i in range (1,((minvalue-1)*2)+1):
        if i%2==0:
            deRifEven.next = startDerif
            startDerif = startDerif.next
            deRifEven = deRifEven.next
        else:
            deRifOdd.next = startDerif
            startDerif = startDerif.next
            deRifOdd = deRifOdd.next
    deRifOdd.next = None
    deRifEven.next = None
    if indexr > size - indexr:
        deRifOdd.next = startDerif
        temp = HeadOdd
        while temp.next != None:
            temp = temp.next
        temp.next = HeadEven
    
    elif indexr < size - indexr:
        deRifOdd.next = HeadEven
        deRifEven.next = startDerif
    
    else:
        deRifOdd.next = HeadEven
    print("Deriffle "+format(r,".3f")+" % : ",end="")
    print(printLL(DerifHead))
    deBottomUpSize = size - indexb
    temp = DerifHead
    DEBottomUpHead = DerifHead
    for i in range(deBottomUpSize-1):
        temp = temp.next
    newHeadDBU = temp.next
    temp.next = None
    finalNewHeadDBU = newHeadDBU
    while finalNewHeadDBU.next != None:
        finalNewHeadDBU = finalNewHeadDBU.next
    finalNewHeadDBU.next = DEBottomUpHead
    print("Debottomup "+format(b,".3f")+" % : ",end="")
    print(printLL(newHeadDBU))

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
