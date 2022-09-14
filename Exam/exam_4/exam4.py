from math import log2
from math import floor

def print90(lists,index,max_i):
    if index<max_i:
        indent = floor(log2(index+1))
        print90(lists,(index*2)+2,max_i)
        print('     '*indent,lists[index])
        print90(lists,(index*2)+1,max_i)

def insertMinHeap(lists,index):
    insertidx = lists[index]
    fi = (index-1)//2
    while index>0 and insertidx < lists[fi]:
        lists[index] = lists[fi]
        index = fi
        fi = (index-1)//2
    lists[index] = insertidx

def deleteMinHeap(lists,last):
    insertidx = lists[last]
    lists[last] = lists[0]
    hole = 0
    ls = hole*2+1
    found = False
    while ls < last and not found:
        rs = ls if ls+1 >= last else ls + 1
        min = ls if lists[ls] < lists[rs] else rs
        if lists[min] < insertidx:
            lists[hole] = lists[min]
            hole = min
            ls = hole*2+1
        else:
            found = True
    lists[hole] = insertidx

lists = list(map(int,input("Enter Input : ").split()))
for i in range(1,len(lists)):
    insertMinHeap(lists,i)
print("Min Heap Array : ",end="")
print(lists)
print("------------------")
print("Array : ",end="")
print(lists)
print90(lists,0,len(lists))
print("------------------")
for l in range(len(lists)-1,0,-1):
    deleteMinHeap(lists,l)
    print("Array : ",end="")
    print(lists)
    print90(lists,0,l)
    print("------------------")
print("Complete Sorted Array : ",end="")
print(lists)
