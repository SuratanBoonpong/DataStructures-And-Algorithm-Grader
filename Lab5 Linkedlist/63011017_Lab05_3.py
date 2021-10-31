
class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    temp = head
    for i in range(1,len(l)):
        nxt = node(l[i])
        temp.next = nxt
        temp = temp.next
    return head

def printList(H):
    temp = H
    while temp!=None:
        print(str(temp),end=" ")
        temp = temp.next
    print()

def mergeOrderesList(p,q):
    if int(p.data) < int(q.data):
        temp = p
        nextNodeP = p.next
        nextNodeQ = q
    else:
        temp = q
        nextNodeP = p
        nextNodeQ = q.next
    head = temp
    while nextNodeP != None or nextNodeQ != None:
        if nextNodeP != None and nextNodeQ != None:
            if int(nextNodeP.data) < int(nextNodeQ.data):
                temp.next = nextNodeP
                temp = temp.next
                nextNodeP = nextNodeP.next
            else:
                temp.next = nextNodeQ 
                temp = temp.next
                nextNodeQ = nextNodeQ.next
        elif nextNodeP != None:
            temp.next = nextNodeP
            temp = temp.next
            nextNodeP = nextNodeP.next
        elif nextNodeQ != None:
            temp.next = nextNodeQ
            temp = temp.next
            nextNodeQ = nextNodeQ.next
    return head

list1,list2 = input("Enter 2 Lists : ").split()
L1 = list1.split(",")
L2 = list2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)